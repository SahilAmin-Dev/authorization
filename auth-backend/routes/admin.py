from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .login import verify_token

router = APIRouter()
security = HTTPBearer()

@router.get("/admin")
def CheckAdmin(credentials:HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = verify_token(token)
    if(payload["role"] == "admin"):
        return {"role":"admin"}
    else:
        return {"role":"user"}
    
