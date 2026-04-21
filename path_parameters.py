#import FastAPI
from fastapi import FastAPI

#initilaised FastAPI application
app = FastAPI()

@app.get("/userdata/{id}") #decorator is used to create an endpoint at the path that listens to GET commands
def data_on_user(id:int): #restricts id to only be a integer value and allows the value of id inputted to be referred to in the function
    if id == 1: #if id is 1 then when going onto the path then this is returned
        return {"data":
        {"firstname" : "John",
         "lastname" : "Smith",
         "id" : id}}
    elif id == 2: #if id is 2 then when going onto the path then this is returned
        return {"data":
        {"firstname" : "Klein",
         "lastname" : "Moretti",
         "id" : id}}

#if the following path is written then the following function is not returned 
#this is because after the dynamic route , FastAPI will attempt to match welcome to the integer data type 
#this happens as everything a path is opened up , FastAPI reads th code line by line and so id being set to being only an integer is done before userdata/welcome is made
#this would fail leading to different output than from what is wanted
@app.get("/userdata/welcome")
def welcome_user():
    return "welcome user"

#in summary a path parameter is a value which can be changed and is present on the decorator which creates an enpoint at a path 
#the parameter can be restricted to different data types and be used in the following function after a decorator

