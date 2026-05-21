from fastapi import APIRouter , Depends , HTTPException , status #
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext 
import all_schemas , tables , database_handling
from JWTdata import * 


login = all_schemas.login
get_db = database_handling.get_db
Session = database_handling.Session
userinfo = tables.user_info
pwd_context = CryptContext(schemes =["bcrypt"] , deprecated = "auto")


def verify(hashedpass , plain_pass):
    return pwd_context.verify(plain_pass , hashedpass)

def login(request : OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(userinfo).filter(userinfo.email == request.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail = "invalid credentials")
    if not verify(user.password ,  request.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail = "invalid credentials")

    #now to generate a JWT token
    #to use thsi soem models/schemas have to be defined and some variables have to be defined 
    #those will be in their respective files
    #the making of the access token is made int the jwt file so now a new access token is made with its expiry date
    access_token  = create_access_token(data =  {"sub" : user.email})
    return {"access_token": access_token, "token_type": "bearer"}