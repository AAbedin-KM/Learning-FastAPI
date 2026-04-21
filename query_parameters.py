#query parameters are used to filter , limit and do more for a single endpoint
#they appear after a ? in the url of a server 
#they are optional and dont affect the path in any way

#import needed modules
from fastapi import FastAPI

from typing import Optional

#initialise app
app = FastAPI()

@app.get("/userdata")
def returnuser(limit : int): #limit is the query parameter and is restricted tio be an integer
  #to access the path on the server u would first go on ur server then add /userdata? and then declare an integer value for limit
  #eg:  /userdata?limit=10&
  #the ? is used to show a query parameter has been used
    return {"message": f"welcome user, right now only {limit} amount of posts are being uploaded"}

@app.get("/TarotClub") 
def conditonal(limit , member = True):
    if member: #the query parameter can be used in logical statements such as if conditions , etc
        return {"member"}
    else:
        return {"not a member "}


#to have a query parameter nto need a value to be passed in you do : [name of query paramter] : Optional[datatype] = None
#Optional is a method from the module typing and therefore needs importing 
@app.get("/Backlund_acityinLOTM")
def condional_one(limit, rich  , beyonder : Optional[Bool] = None):
    return f"limit = {limit} , rich = {rich} , beyonder = {beyonder}"

#the difference between a path parameter and a query parameter is that a path parameter affects the path itself whilst a query parameter only effects
#what is returned when accessing the path

