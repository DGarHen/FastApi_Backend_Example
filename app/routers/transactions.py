from fastapi import HTTPException, status, APIRouter
from models import *
from db import *
from sqlmodel import *

router = APIRouter(tags=['Transactions'])

@router.post("/transactions")
async def createTransaction(transactionData: TransactionCreate, session: SessionDep):
    transactionDataDict = transactionData.model_dump()
    customer = session.get(Customer, transactionDataDict.get('customer_id'))
    if not customer:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Error, Transaction's customer was not found.")
    
    transactionDb = Transaction.model_validate(transactionData.model_dump())
    session.add(transactionDb)
    session.commit()
    session.refresh(transactionDb)
    return transactionDb

@router.get("/transactions", response_model=list[Transaction])
async def getTransactions(session: SessionDep):
    return session.exec(select(Transaction)).all()

@router.get("/transactions/{transactionId}", response_model=Transaction)
async def getTransactions(transactionsId: int, session: SessionDep):
    transactionDb = session.get(Transaction, transactionsId)
    if not transactionDb:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Error, Transaction was not found.")
    
    return transactionDb


