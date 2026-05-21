from fastapi import FastAPI

app = FastAPI()

@app.get("/userdata/{id}")
def data_on_user(id:int): #this sets id to only be an integer in which when u try searrch for a page with the id it can only be an integer
    #when going into the local host you cna pass any value into the parameter and a page apart of the host will open with the value of the parameter u inputed
    if id == 1:
        return {"data":
        {"firstname" : "Aliff",
         "lastname" : "Abedin",
         "id" : id}}
    elif id == 2:
        return {"data":
        {"firstname" : "Ahnaff",
         "lastname" : "Abedin",
         "id" : id}}

#fast api reads the code line by line
#so in this case if i were to make another page of suerdata after userdata and have it be a string
#and then searched for it an error woudl show up as intially the page belonging to user data is first amde to be an integer and so fast api follows that instead of the string one u intended to use

#to bypass this you make an7 pages belonging to one page before the page which requires a vertain data type 
#eg:

@app.get("/userdata/welcome")
def welcome_user():
    return "welcome user"

#if i ran the function above rn it wouldnt work 
#and so to fix this I would have to put it before to bypass the action of needing the data ionputed to be of a certain data type

#for the future u can test if the code works fro example parameter handling by using localhost/ur number /docs#
