from sqlmodel import SQLModel, Field as ModelField
from typing import Optional
from pydantic import BaseModel, Field

class User(SQLModel, table=True):
	id: Optional[int] = ModelField(default=None, primary_key=True)
	username: str = ModelField(index=True, unique=True)
	hashed_password: str 

class CreateUserSchema(BaseModel):
	username: str = Field(..., min_length=6)
	password: str = Field(..., min_length=6)
	confirmation: str = Field(..., min_length=6)