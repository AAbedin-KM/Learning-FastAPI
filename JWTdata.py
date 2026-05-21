from jose import jwt , JWTError
from datetime import datetime, timedelta
from all_schemas import *

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data : dict):
    to_encode = data.copy() #returns a copy of the data passed in 
    expire = datetime.utcnow() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp" : expire})
    encoded_jwt = jwt.encode(to_encode , SECRET_KEY , algorithm = ALGORITHM)

    return encoded_jwt


def verifytoken(token : str , credentials_exception):
    try:
        payload = jwt.decode(token , SECRET_KEY , algorithms = [ALGORITHM])
        email : str = payload.get("sub") #thsi stores the email from the sub and if there isnt an email then 
        if email is None:
            raise credentials_exception #error is raised
        token_data = TokenData(email = email)  #stores the returned in the form of a strcutured schema
    except JWTError: #if the jwt token is not been verified then exception is raised
            raise credentials_exception
    