from fastapi import APIRouter,HTTPException
from sqlmodel import select
from app.dependencies import SessionDep
from typing import List
from app.user.model import CreateUserSchema, User
from fastapi import APIRouter, HTTPException
from sqlmodel import select
from app.auth.utils import get_password_hash


router = APIRouter(prefix="/api/v1/users", tags=["Users"])

@router.get("/", response_model=List[User])
def get_users(session: SessionDep):
    users = session.exec(select(User)).all()
    return users

@router.post("/", response_model=None)
def create_user(user_data: CreateUserSchema, session: SessionDep):
    existing_user = session.exec(select(User).where(User.username == user_data.username)).first() 
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_pw = get_password_hash(user_data.password)
    new_user = User(username=user_data.username, hashed_password=hashed_pw)
    
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return {"message": "User created successfully", "user": new_user}