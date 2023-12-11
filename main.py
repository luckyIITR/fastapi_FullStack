from fastapi import FastAPI, Request
from starlette import status
from starlette.responses import HTMLResponse, RedirectResponse

import models
from database import engine
from routes import auth, todos
from starlette.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)


# app.include_router(admin.router)
# app.include_router(users.router)

@app.get("/", response_class=HTMLResponse)
async def authentication_page(request: Request):
    return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)
