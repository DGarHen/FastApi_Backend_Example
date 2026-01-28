from sqlmodel import Session, create_engine, SQLModel
from typing import Annotated
from fastapi import Depends, FastAPI

sqlite_name = "db.sqlite3"
sqlite_url = f"sqlite:///{sqlite_name}"

engine = create_engine(sqlite_url)

def createAllTables(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

def getSession():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(getSession)]