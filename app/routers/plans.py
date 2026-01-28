from fastapi import HTTPException, status, APIRouter
from models import *
from db import *
from sqlmodel import *

router = APIRouter(tags=['Plans'])

@router.post("/plans", response_model=Plan)
async def createPlan(planData: Plan, session: SessionDep):
    planDb = Plan.model_validate(planData.model_dump())
    session.add(planDb)
    session.commit()
    session.refresh(planDb)
    return planDb

@router.get("/plans", response_model=list[Plan])
async def getPlans(session: SessionDep):
    return session.exec(select(Plan)).all()