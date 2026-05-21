#to actualy make it so that a person has to log into an account before accessing anything 
#we use oath2

from fastapi import Depends , HTTPException , status
from fastapi.security import OAuth2PasswordBearer
from JWTdata import *


#first the jwt token has to be referred to and passed throught the oath2
#this is done by:
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "Authentication/login") #the token url refers to the endpoint where the token will be returned from


def get_current_user(token : str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED , 
        detail = "could not validate credentials",
        headers = {"WWW-Authenticate" : "Bearer"}
    )
    #the token is now needed to be verified and if verified returns true it is then decoded 
    #if verification returns false return the credetnials exception showing that the data inputted by the user is invalid 
    return verifytoken(token , credentials_exception)


#summary of oath2 useage:
#allows the confirmation of logging in via a jwt token 
#a jwt token is created for each user when they log in
#in the code a function which creates teh jwt token is referred to when logging in , it uses the username of the person whcih is just the email as the anchor to which it creates a jwt token
#when loggin ine the authentication function has the othpasswordform schema 
#this means that instead of the traditonal format of entering data into the dropdown menu in swagger ui 
#there is a form u can fill in 
#this can be used to lock certain queries and actions which can be done 
#for example posting soemthing toa  databse may require you to login in in whcih you know how to log in 
#in practical code this works by first assinging a variable and then the format it should be formatted in (which is just the scema) and then have ti depend on the on the function which retrieves the user based on the jwt token 
#in terms of how data is trasnferred and referred to , a function corersponding to one endpoint depends on the get current user
#the current user function then gets the token from which was retruned from when the user first logged in 
#in this code when i logged in a jwt token was created based on my user name , so now fastapi knows who i am
#this can now allow entry to the queries i want to interact with 
#specifically the jwt token is retrieved by finding out where the jwt token wsas generated in terms fo endpoint and then gettign the value retruned from the fucntion corresponding to that endpoint 
#and then passing that itno the getcurentuser function which verifes the user 
