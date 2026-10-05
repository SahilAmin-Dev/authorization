from fastapi import FastAPI
from routes.login import router as login_router
from routes.admin import router as admin_router

app = FastAPI()
app.include_router(login_router)
app.include_router(admin_router)
