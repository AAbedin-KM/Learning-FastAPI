from pydantic import BaseModel
from typing import Optional

class post(BaseModel):
    favouritecharacter: str
    reason: str
    rating: Optional[int] = None
    user_id: Optional[int] = None
    class Config:
        orm_mode = True

class Usernames_passwords(BaseModel):
    name : str
    DOB : str
    email: str
    username : str
    password : str

#making wrapper to then be applied onto the returned result 
#will be used to hide id 
class id_hider(BaseModel):
    name : str
    DOB : str
    email : str
    username : str 
    password : str
    class Config:
        orm_mode = True

# Schema to represent the user info embedded inside a post response      
class UserInPost(BaseModel):
    name: str
    username: str
    email: str
    posts : list[post] = []
    class Config:
          orm_mode = True

class login(BaseModel):
    username : str 
    password : str 

class Token(BaseModel):
    access_token : str
    token_type : str 

class TokenData(BaseModel):
    email : Optional[str] = None

