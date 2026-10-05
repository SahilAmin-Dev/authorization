from fastapi import APIRouter
from database import collection
from models import LoginData
from pwdlib import PasswordHash
from jose import jwt
password_hash = PasswordHash.recommended()

SECRET_KEY = "my-secret-key"
ALGORITHM = "HS256"


router = APIRouter()

@router.post("/login")
def login(data:LoginData):
    
    user = collection.find_one({"name" : data.name})

    if user is None:
         return {"message": "User not found"}
    stored_hash = user["hashedPassword"]

    if not password_hash.verify(data.password, stored_hash):
         return {"message":"incorrect password"}

    payload = {
        "user_id":str(user["_id"]),
        "name":user["name"],
        "role":user["role"]
   }
    token = jwt.encode(
         payload,
         SECRET_KEY,
         algorithm=ALGORITHM
    )
    return token    
         
