from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.dependencies import get_session
from app.user.model import User
from sqlmodel import select
from app.auth.utils import SECRET_KEY, ALGORITHM
from jwt import decode
from jwt.exceptions import InvalidTokenError
from typing import Annotated
from sqlmodel import Session
from fastapi import Depends

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)],
    session: Annotated[Session, Depends(get_session)]
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception

    user = session.exec(select(User).where(User.username == username)).first()
    if user is None:
        raise credentials_exception
    return user

