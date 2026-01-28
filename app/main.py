from fastapi import FastAPI, HTTPException, status
from models import *
from db import *
from sqlmodel import *
from .routers import customers, transactions, invoices, plans

app = FastAPI(lifespan=createAllTables)
app.include_router(customers.router)
app.include_router(transactions.router)
app.include_router(invoices.router)
app.include_router(plans.router)