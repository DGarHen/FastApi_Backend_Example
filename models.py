from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Relationship
from enum import Enum

class StatusEnum(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class CustomerBase(SQLModel):
    name: str = Field(default=None)
    description: str = Field(default=None)
    email: str = Field(default=None)
    age: int = Field(default=None)

class CustomerCreate(CustomerBase):
    pass

class CustomerPlan(SQLModel, table=True):
    id: int = Field(primary_key=True)
    planId: int = Field(foreign_key="plan.id")
    customerId: int = Field(foreign_key="customer.id")
    status: StatusEnum = Field(default=StatusEnum.ACTIVE)

class Plan(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    name: str = Field(default=None)
    price: int = Field(default=None)
    description: str = Field(default=None)
    customers: list["Customer"] = Relationship(back_populates="plans", link_model=CustomerPlan)

class Customer(CustomerBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    transactions: list["Transaction"] = Relationship(back_populates="customer")
    plans: list["Plan"] = Relationship(back_populates="customers", link_model=CustomerPlan)

class CustomerUpdate(CustomerBase):
    pass


class TransactionBase(SQLModel):
    ammount: int = Field(default=None)
    description: str = Field(default=None)  

class Transaction(TransactionBase, table=True):
    id: int = Field(default=None, primary_key=True)
    customer_id: int = Field(default=None, foreign_key="customer.id")  
    customer: Customer = Relationship(back_populates="transactions")

class TransactionUpdate(TransactionBase):
    pass

class TransactionCreate(TransactionBase):
    customer_id: int = Field(default=None, foreign_key="customer.id")

class Invoice(BaseModel):
    id: int
    customer: Customer
    transactions: list[Transaction]
    total: int 
    @property
    def total(self):
        return sum(transaction.ammount for transaction in self.transactions)