from fastapi import HTTPException, status, APIRouter
from models import *
from db import *
from sqlmodel import *

router = APIRouter(tags=['Invoices'])

@router.post("/invoices")
async def createCustomer(invoiceData: Invoice):
    return invoiceData