
from fastapi import HTTPException, Query, status, APIRouter
from models import *
from db import *
from sqlmodel import *

router = APIRouter(tags=['Customers'])

@router.post("/customers", response_model=Customer, status_code=status.HTTP_201_CREATED)
async def createCustomer(customerData: CustomerCreate, session: SessionDep):
    customer = Customer.model_validate(customerData.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

@router.get("/customers", response_model=list[Customer])
async def getCustomers(session: SessionDep):
    return session.exec(select(Customer)).all()

@router.get("/customers/{customerId}", response_model=Customer)
async def getCustomers(customerId: int, session: SessionDep):
    customerDb = session.get(Customer, customerId)
    if not customerDb:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Error, Customer was not found")
    
    return customerDb

@router.delete("/customers/{customerId}")
async def deleteCustomer(customerId: int, session: SessionDep):
    customerDb = session.get(Customer, customerId)
    if not customerDb:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Error, Customer was not found")
    
    session.delete(customerDb)
    session.commit()
    return {"detail":"ok"}

@router.patch("/customers/{customerId}", response_model=Customer, status_code=status.HTTP_202_ACCEPTED)
async def updateCustomer(customerId: int, customerData: CustomerUpdate, session: SessionDep):
    customerDb = session.get(Customer, customerId)
    if not customerDb:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Error, Customer was not found.")
    customerDataDict = customerData.model_dump(exclude_unset=True)
    customerDb.sqlmodel_update(customerDataDict)
    session.add(customerDb)
    session.commit()
    session.refresh(customerDb)
    return customerDb

@router.post("/subscribe/{customerId}/plan/{planId}", response_model=CustomerPlan)
async def subscribeCustomerToPlan(customerId: int, planId: int, session: SessionDep,
                                  planStatus: StatusEnum = Query()):
    customerDb = session.get(Customer, customerId)
    if not customerDb:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Error, Customer was not found.")
    planDb = session.get(Plan, planId)
    if not planDb:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Error, Plan was not found.")
    
    customerPlanDb = CustomerPlan(customerId=customerDb.id, planId=planDb.id, status=planStatus)
    session.add(customerPlanDb)
    session.commit()
    session.refresh(customerPlanDb)
    return customerPlanDb

@router.get("/customer/{customerId}/plan/", response_model=list[Plan])
async def getCustomersPlans(session: SessionDep, customerId: int, statusPlan:StatusEnum = Query()):
    customerDb = session.get(Customer, customerId)
    if not customerDb:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Error, Customer was not found.")
    query = select(CustomerPlan).where(CustomerPlan.customerId == customerId).where(CustomerPlan.status == statusPlan)
    queryPlans = session.exec(query).all()
    return customerDb.plans