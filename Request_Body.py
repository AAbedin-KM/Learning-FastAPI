#POST function in FastAPI allows a person to create a path and have a query be displayed
#for example a new paths endpoint called favouritecharacter is created but theres currently theres no info on the path 
#so lets add some info into the path
#import modules
from fastapi import FastAPI
from pydantic import BaseModel #comes with FastAPI
from typing import Optional 

app = FastAPI()

#when creating a post u cant directly pass in paramters
#instead u can pass in classes which contain parameters u can give values to 
#this is done below

#this class gives the structure of the query in which all POST commands needs this 
#this is called a schema
class FavouriteCharacter(BaseModel): #inherits from parent class BaseModel (if you want more info look into inheritance which is apart of OOP)
    character : str
    reason : str
    how_much_out_of_ten : int
    eaten : Optional[bool]

@app.post("/favoritecharacter") #creation of a path 
def favourite_character(request:FavouriteCharacter): #query at that path
    return request , f"myfavourite character is {request.character} and this is because {request.reason}
    and I rate the character a {request.how_much_out_of_ten}/10)") 
    #the schema itself and the statement is returned
    #u can refer to the values stored in the schema as long as u refer to the schema first
