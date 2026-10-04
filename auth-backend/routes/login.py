from fastapi import APIRouter
from database import collection
from models import LoginData
from pwdlib import PasswordHash


router = APIRouter()

@router.post("/login")
def login(data:LoginData):
    user = collection.find_one({data.name})

    if user is None:
         return {"message": "User not found"}
    
