from fastapi import FastAPI

app = FastAPI()

from routes.login import router as login_router

app = FastAPI()

app.include_router(login_router)