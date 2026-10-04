from pydantic import BaseModel

class LoginData(BaseModel):
     name:str
     password:str