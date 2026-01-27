from fastapi import FastAPI
from models import *
app = FastAPI()


@app.get("/")
def read_root():
    return {"mensaje": "Hola Mundo", "estado": "funcionando"}

@app.post("/customers")
async def createCustomer(customerData: Customer):
    return customerData

@app.post("/transactions")
async def createTransaction(transactionData: Transaction):
    return transactionData

@app.post("/invoices")
async def createCustomer(invoiceData: Invoice):
    return invoiceData