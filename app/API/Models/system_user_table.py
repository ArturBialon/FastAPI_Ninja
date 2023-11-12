from pydantic import BaseModel
from sqlalchemy import MetaData, Column, Integer, String
from sqlalchemy.orm import declarative_base

metadata = MetaData()

Base = declarative_base(metadata=metadata)

class SystemUser(Base):
    __tablename__ = "SystemUser"

    Id = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    Password = Column(String)
    Role = Column(Integer)
    
class GetSystemUserDTO(BaseModel):
    id: int
    name: str
    role: str
    
class AccessToken(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    user_name: str or None = None
    

