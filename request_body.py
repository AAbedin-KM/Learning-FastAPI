#POST function in FastAPI allows a eprson to create a new page for the host
#for example a new page called potatoes could be made and not just retrived
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional 

app = FastAPI()

class Potatoes(BaseModel):
    title : str
    body : str
    amount : int
    eaten : Optional[bool]

@app.post("/potatoes")
def create_potatoes(request:Potatoes):
    return request , f"title: {request.title} is out for cinemas"

#when creating a post u cant directly pass in paramters
#instead u can pass in objects which contain parameters u can fill in 
#an example of this is above 
#to output the actual request beign uploaded u have to return it
#the values whcih are used and stored in the class can be referred to 


