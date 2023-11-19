from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from app.API.Controllers import user_controller
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(user_controller.router)
app.mount("/static", StaticFiles(directory="app/static"), name="static")


