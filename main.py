from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.API.Authorization.auth import LoginForm
from app.API.Controllers import user_controller
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(user_controller.router)
    
@app.get("/about")
def about():
    return "All you need to know about DPR"

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def show_form(request: Request):
    form = LoginForm()
    return templates.TemplateResponse("question.html", {"request": request, "form": form})

@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    form = LoginForm()
    return templates.TemplateResponse("login.html", {"request": request, "form": form})

@app.post("/login")
async def process_login(request: Request, form: LoginForm):
    # Perform login logic here
    # Redirect or return a response based on the login result
    return {"message": "Login successful"}

