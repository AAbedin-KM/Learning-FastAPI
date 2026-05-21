from fastapi import FastAPI , Depends , status ,Response , HTTPException
from pydantic import BaseModel
from typing import Optional 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column , Integer , String , ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
app = FastAPI()

class food(BaseModel):
    potatoes: str
    steak : str 
    hungry : bool


#@app.post("/pydanticschema") #whenever u do a post request and then go ontio the website it will display emthod not available
#def func_one(request: food):
    #return f"my {request.potatoes} and my {request.steak}"

#to first store data into a databsse u need to run the dtabase and then dictate where the database wil be 
#to first connect to a databse whihc fastapi can interact with u can use sqlalchemy 
#then the dtaabase would be postgressql 

#to first do this we have to actualy instantialise the engine 
SQLALCHAMY_DATABASE_URL = 'sqlite:///./tutorial.db'
engine = create_engine(SQLALCHAMY_DATABASE_URL , connect_args={
                       "check_same_thread": False})

#now u make the session 
sessionlocal = sessionmaker(bind = engine , autocommit = False , autoflush = False)

#now u make the base
Base = declarative_base()

# import models AFTER Base is defined so tables.py can import Base without a circular import

#to then instantialise it so that the tables are actually been made
Base.metadata.create_all(bind = engine )

#this actualy returns the session 
#the session is then passed into Depends() to turn into a pydantic object (used in the function later on)
def get_db():
    db = sessionlocal() #makeing the session object 
    try: yield db
    finally:
        db.close()

#to actualy create the database whenever the server is started:
#@app.post("/database_tutorial" , status_code = 201)
#def create_table(request : food , db : Session = Depends(get_db)):
    #to actualy carry the database into a post we first have to make it a pydantic object
    #what will be done is making a new schema and fill in the info
    #then u add that info into the database
    #new_food_entry = table_one(title = request.potatoes , body = request.steak) #map pydantic data onto the SQLAlchemy model
    #table_one is the table in the database and u are filling one cell in each column by referrign to the column and then the value u want the cell to be in
    #db.add(new_food_entry) #adding the obnject with info into the database
    #db.commit() #tp execute the modification of the database
    #db.refresh(new_food_entry) #to actually update the database so the info added shows up in the database
    #return new_food_entry

#now to actually retrive a set of data from the table
#@app.get("/database_retrieval")
#def get_data(response : Response ,db : Session = Depends(get_db)):
    #data = db.query(table_one).all() #this access all teh queries in the database in the table table_one
    #if data:
        #response.status_code = status.HTTP_200_OK
        #return "the shit has been found"

    #return data #retruns the data stored in the data variable

#to then retrieve one peice of data:
#we use the primary key to get one piece of data
#@app.get("/database_retrieval_singular")
#def get_singular(id , response: Response , db : Session = Depends(get_db)):
    #singular_data = db.query(table_one).filter(table_one.id == id).first()#gets all data in the table table_one and then filters the data by finding where the column equals the id and then the first peice of data witht eh id is returned
     #filter() is used to allow data to be found via conditions
    #if not singular_data:
        #response.status_code = status.HTTP_404_NOT_FOUND
        #to do this a better way and return a comment and have the other stuff retuirn
        #you use HTTPException
        #raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail = f"well theres no data with the id {id}")

    #return singular_data

#exception and status code
#exception and status code may be changed to fit the actual operation and task which has been done 
#for example when adding a data onto a table in a dataset you would rather have the code be 201 whucih means created insetad of 200 which measn ok
#as new data has been created and added onto the 201 code is mroe suited to it 
#to do this u just do status_code = [number]
#u can find ur wanted code by imporint status and tehn typing up the name and it should be returned
#with repsonse codes it dictates the the execution of an action doen by a fucntion 
#however the result of the function may not be as expected 
#in this case what we do is when usign the decorator have the status_code be the default 
#then in the function belonging decorator u do this:
#checking if any conditions is not ebign met
#if so then response.status_code = status.[the needed status code]
#u need to pass in response and have it be the Response modlule 
#you can thenr return a soemthign afertwards 
#however to do this in a more efficient way you use HTTPException()
#you just pass in the status_code you want and what message iu want to return using detail = "[string]"

#to delete a blog:
#first link an action to the server using @app.delete()
#@app.delete("/database_delete{id}")
#def data_delete(id , response : Response, db : Session = Depends(get_db)):
    #delete_data = db.query(table_one).filter(table_one.id == id)
    #if not delete_data:
        #raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail = f"data with id {id} is not found")
    #else:
        #delete_data.delete(synchronize_session = False)
        #db.commit()

    #return delete_data , "has been deleted"


#to update data fro-m a database:
#first u do a put operation
#@app.put("/database_update{id}")
#def data_update(id ,request : food,  response : Response , db : Session = Depends(get_db)):
    #data = db.query(table_one).filter(table_one.id == id)
    #if not data.first:
        #raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail = f"data with {id} is not found")
    #else:
        #data.update({"title" : request.potatoes}) #u filter it and then u use update()
    #in {} brackets u referto teh columns in the table and then have them equal to what data u want to pass it
    #that data is dictated by the shceme u carried in which is what the info from the table is based off of
    #if u want to change the value of all columns for that specific id you dont need to specify which col;umsnto change in {}
    #you can just pass in the entire request
        #db.commit()

    #return "updated"

