from datetime import timedelta
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.API.Authorization.auth import TOKEN_EXP_MIN, create_access_token, get_hashed_password, verify_password
from app.API.Models.system_user_table import AccessToken, SystemUser, GetSystemUserDTO
from app.API.database import session_local

router = APIRouter()


@router.get("/users")
async def read_users():
    session = session_local()
    users = session.query(SystemUser.Name).all()
    names = [user[0] for user in users]
    result = names
    if result is None:
        raise HTTPException(status_code=404, detail="Users not found")
    session.close()
    return result


@router.get("/users/{user_id}")
async def read_users(user_id: int):
    session = session_local()
    
    user = session.query(SystemUser).where(SystemUser.Id == user_id).first()
    result: GetSystemUserDTO = {
        user.Id, 
        user.Name, 
        user.Role
        }
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    session.close()
    return result

@router.post("/users/token", response_model=AccessToken)
async def login_for_access(form_data: OAuth2PasswordRequestForm=Depends()):
    session = session_local()
    user = session.query(SystemUser).where(SystemUser.Name == form_data.username).first()
    session.close()
    if not user:
        return False
    if not verify_password(form_data.password, user.Password):
        raise HTTPException(status_code=401,
                             detail="Icorrect username or password",
                             headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=TOKEN_EXP_MIN)
    access_token = create_access_token(
        data={"sub": user.Name}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

