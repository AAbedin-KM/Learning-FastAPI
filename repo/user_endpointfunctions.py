from passlib.context import CryptContext
from fastapi import APIRouter , Response , Depends , HTTPException
import all_schemas , tables , database_handling
from typing import List

#repo can be used to store all the functions the endpoints wioll use to actually cause soemthing to happen 
#so when definding the endpoints and their corresponding functions u can refer to the functions stored in the files inside of the repo 
#this allows for the code for the endpoints to be more easily readable and quicker to code as now it conly comes to referring to the functions which have been written before in
#different file

#I wont be doing this for every single endpoint but i will do it for one endpoint for user and posts 
#the user example is down below 
#the user example will bein post_endpointfunction.py



Usernames_passwords = all_schemas.Usernames_passwords
Session = database_handling.Session
pwd_context = CryptContext(schemes =["bcrypt"] , deprecated = "auto")
user_info = tables.user_info

def create_user(request : Usernames_passwords , db:Session):
    hashedpassword = pwd_context.hash(request.password)
    new_user_info = user_info(name = request.name , DOB = request.DOB , username = request.username , 
    email = request.email , password = hashedpassword)
    db.add(new_user_info)
    db.commit()
    db.refresh(new_user_info)
    
    return new_user_info