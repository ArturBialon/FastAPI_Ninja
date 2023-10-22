from sqlalchemy import MetaData, Column, Integer, String, BINARY
from sqlalchemy.orm import declarative_base

metadata = MetaData()

Base = declarative_base(metadata=metadata)

class SystemUser(Base):
    __tablename__ = "SystemUser"

    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    Password = Column(BINARY)
    PasswordSalt = Column(BINARY)
    Role = Column(Integer)
