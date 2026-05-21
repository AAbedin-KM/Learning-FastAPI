from fastapi import FastAPI , Depends , status ,Response , HTTPException
from pydantic import BaseModel
from typing import Optional 
from database_handling import table_one , get_db , food , engine , Base
import uvicorn 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column , Integer , String , ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from passlib.context import CryptContext
from tables import user_info


app = FastAPI()

Base.metadata.create_all(bind = engine )

#making schema for the username and password whcih will then be added into the database later on 
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
    DOB: str
    class Config:
          orm_mode = True

class PostResponse(BaseModel):
    id: int
    title: str
    body: str
    user_id: int
    userinfo: UserInPost   # <-- this uses the relationship
    class Config:
        orm_mode = True

@app.get("/posts/{id}", response_model=PostResponse, tags=["posts"])     
def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(table_one).filter(table_one.id == id).first()        
    if not post:
        raise HTTPException(status_code=404, detail=f"Post with id {id} not found")
    return post


pwd_context = CryptContext(schemes =["bcrypt"] , deprecated = "auto")
@app.post("/user" , response_model = id_hider , tags=["user_handling"])
def create_user(request : Usernames_passwords , db : Session = Depends(get_db)):
    hashedpassword = pwd_context.hash(request.password)
    new_user_info = user_info(name = request.name , DOB = request.DOB , username = request.username , 
    email = request.email , password = hashedpassword)
    db.add(new_user_info)
    db.commit()
    db.refresh(new_user_info)
    
    return new_user_info

#to make a path and query which lets u access a user by typing in a specific id in the path 
@app.get("/user/{id}" , response_model = id_hider ,tags=["user_handling"])
def get_user_by_id(id : int , response : Response , db : Session = Depends(get_db)):
    wanted_userdata = db.query(user_info).filter(user_info.id == id).first()
    if not wanted_userdata:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail = f"user with id: {id} is not valid")
    else:
        return wanted_userdata



#using doc tags:
#doc tags allow for endpoints to be palced under headings 
#this allows for a mroe clear represnetation of all endpoints beign created as they are ordered udner tags 
#which cna be toggled on or off to only see paths which are needed
#this is done by writing:
#tags = ["name of tag"] after the path in the decorator 

#relationships:
#relationships in terms fo databases is how databases aer related to each other
#for example two tabkes can be linked together with one key 
#yhat key is a foreign key 
#for example there are two tables: userdata table and a posts '
#a user can have multiple posts but a post cant have multiple posts 
#therefore the relationsuip is one to many as user can have many posts but one post cant have many users
#the key which links the two tables is called the foreign key 
#in this example userid is the foreign key 
#a foreign key is the primary key for another table 
#to implement the table in python:
    #import Relationships from SQlAlchemy
    #locate the schemas for the database table 
    #[variable] = relationship("[name]" , back_populates ="[name of the other table]")
    #do this for both tables
