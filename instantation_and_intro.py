from fastapi import FastAPI

app = FastAPI()#used to create the instance of app
#tye variabel fo the app is important as it is what uvicorn looks for in the file to then make the isnatnce 
#as well as the decorators whcih connect the app to the local host
#so when u change the variable identifier you have to change the call tio run the app , the decorators


@app.get("/") #this acc connects the app to the host make it so that the fucntion is ran

def index():
    #return "olaaa" #as jsons are nronaltl returned in the form of dictionaries lets use dictionaries
    return {
        "data" : {"first_name": "Aliff" , "Last_name": "Abedin"}}

#you an make differnt connections to the same hsot by connectuing the app to the local host via:
#[app].get("/[name of place u want the locla host to have]")
#eg:

@app.get("/intro") #this makes a different page of the local host so now there is the default page and then the page "intro"
def intro_to_self():
    return "I am Aliff Abedin , a 17 year old chud"

#the name of the fucntions being used doesnt really matter in terms of the actual about fucntioning and returning what needs to be returned
#the only thing which matters it thjat it is a sensible identifier

#.get() is a request where the app is connected to the path 
#uvicorn first needs to refer to the module the app instance is currently at 
#this is so that it knows where to find the instance to run 
#.get() is an operation 
#@app is an path operation 


