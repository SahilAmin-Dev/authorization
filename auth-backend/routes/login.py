from fastapi import APIRouter, Depends, HTTPException
from database import collection
from models import LoginData
from pwdlib import PasswordHash
from jose import JWTError, jwt
password_hash = PasswordHash.recommended()
from fastapi.security import OAuth2PasswordBearer , HTTPBearer,HTTPAuthorizationCredentials

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
security = HTTPBearer()

SECRET_KEY = "my-secret-key"
ALGORITHM = "HS256"


router = APIRouter()

def verify_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

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
         
@router.get("/profile")
def profile (credentials:HTTPAuthorizationCredentials = Depends(security)):
     token = credentials.credentials
     payload = verify_token(token)
     return {
        "message": "Access granted",
        "user_id": payload["user_id"]
    }  