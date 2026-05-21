#query parameter is used to handle the fact of there being alot of pages apsrt of one page 
#in which is is comutationally and in general inefficient to load all of them at the same time whenc alling upon the page this holds all the otehr pages

from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/userdata")
def returnuser(limit : int):
    return {"message": f"welcome user, right now only {limit} amount of posts are being uploaded"}

#remidner to me:
    #whenerv i make a new file adn re run make sure the last insatcne is fully closed i only run it on the curent file im on 

#you cna combine multiple parameters and have them used in conditonals to present differnt data 

@app.get("/chudsquared")
def conditonal(limit , chud = True):
    if chud:
        return {"haha u chud"}
    else:
        return {"haha us baka"}

#whenever u set one paramter in the function a default value 
#u have to set up every other paramter a default value
#to bypass this what uc an do is [parameter] = optional[datatype]= None
#to use optinal u have to import Optional from typing
#eg

@app.get("/chudcubed")
def condional_one(limit, chud, sorted : Optional[str] = None):
    return f"limit = {limit} , chud = {chud} , sort = {sorted}"


#the difference between a path parameter and a quiery paramter is that a query paramter only manipulates the amount of queries which show up form a path on the host
#wheras the path paramter manipulates teh path in whcih a new page from an existing page cna be dictated and formed by usign a path parameter 
#eg a new page from chudcubed could be different ids of different chuds 
#and limit woudl be the amount of queiries which pop up on one of those pages in whcih limit is defined in the function 

