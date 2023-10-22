from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.API.Controllers import userController
from app.API.databse import SessionLocal

from app.API.Models.testTable import SystemUser


app = FastAPI()
app.include_router(userController.router)

@app.get("/about")
def about():
    return "All you need to know about Simple Blog"

fake_posts_db = [{
    'title': 'First Blog Post',
    'content': 'Content of the first blog post.',
    'author': 'John Doe',
    'publication_date': '2023-06-20',
    'comments': [
        {'author': 'Alice', 'content': 'Great post!'},
        {'author': 'Bob', 'content': 'Intresting read.'}
    ],
    'status': 'published'
},{
    'title': 'Second Blog Post',
    'content': 'Content of the second blog post.',
    'author': 'Jane Smith'
}]


templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_posts(request: Request):
    return templates.TemplateResponse("question.html", {"request": request, "posts": fake_posts_db})