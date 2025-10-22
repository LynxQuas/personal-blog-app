import os
from typing import Annotated
from dotenv import load_dotenv
from sqlmodel import Session
from fastapi import Depends
from sqlmodel import SQLModel, create_engine, Session


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    SQLModel.metadata.create_all(engine)
    
SessionDep = Annotated[Session, Depends(get_session)]