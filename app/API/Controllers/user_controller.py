from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.API.Authorization.auth import LoginForm
from fastapi.security import OAuth2PasswordRequestForm
from app.API.Authorization.auth import TOKEN_EXP_MIN, LoginForm, create_access_token, get_hashed_password, verify_password
from app.API.Models.system_user_table import AccessToken, SystemUser, GetSystemUserDTO
from app.API.database import session_local

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/users")
async def read_users():
    session = session_local()
    users = session.query(SystemUser.Name).all()
    names = [{user.Name, user.Password} for user in users]
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


@router.post("/login", response_model=None)
async def login_for_access(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    encoded_jwt = ""
    form = LoginForm()
    error_message = ""
    
    session = session_local()
    user = session.query(SystemUser).where(
        SystemUser.Name == form_data.username).first()
    session.close()
    if not user:
        error_message = "Incorrect username or password"
    elif not verify_password(form_data.password, user.Password):
        error_message = "Incorrect username or password"
    else:
        access_token_expires = timedelta(minutes=TOKEN_EXP_MIN)
        encoded_jwt = create_access_token(
            data={"sub": user.Name}, expires_delta=access_token_expires
        )
    return templates.TemplateResponse("question.html", {"request": request, "encoded_jwt": encoded_jwt, "form": form, "error_message": error_message})


@router.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    encoded_jwt = ""
    form = LoginForm()
    return templates.TemplateResponse("question.html", {"request": request, "encoded_jwt": encoded_jwt, "form": form})
