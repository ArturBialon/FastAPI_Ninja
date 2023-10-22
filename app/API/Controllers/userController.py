from fastapi import APIRouter, HTTPException
from app.API.Models.testTable import SystemUser
from app.API.databse import SessionLocal

router = APIRouter()

@router.get("/users")
async def read_users():
    session = SessionLocal()
    users = session.query(SystemUser.Name).all()
    names = [user[0] for user in users]
    result = names
    if result is None:
        raise HTTPException(status_code=404, detail="Users not found")
    session.close()
    return result