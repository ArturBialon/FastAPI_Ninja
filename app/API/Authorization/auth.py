
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import JWTError, jwt
from app.API.Models.system_user_table import SystemUser

from app.API.database import session_local
from app.API.Models.system_user_table import TokenData

HASH_KEY = "6c20cae15f8ebec1dd697ba77733f7f1659270e062b1985c8424f68ff62ea7ff" #that should be stored somwhere safe, like system ENV Variables
TOKEN_EXP_MIN = 60000
ALG = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_hashed_password(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta or None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
        
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, HASH_KEY, algorithm=ALG)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth_2_scheme)):
    credential_exception = HTTPException(status_code=401, 
                                         detail="Credentials could not be validated", 
                                         headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, HASH_KEY,algorithms=[ALG])
        user_name: str = payload.get("sub")
        if user_name is None:
            raise credential_exception
        token_data = TokenData(user_name=user_name)
    except JWTError:
        raise credential_exception
        
    session = session_local()
    user = session.query(SystemUser).where(SystemUser.Name == token_data.user_name).first()
    if user is None:
        raise credential_exception
    session.close()
    
    return user
    
    