from fastapi import FastAPI , Depends , status ,Response , HTTPException
from pydantic import BaseModel
from typing import Optional 
from database_handling import table_one , get_db , food

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column , Integer , String
from sqlalchemy.orm import Session

app = FastAPI()

#reponse scheme is just the response model

#as singualr_data returns the id and we dont want it to return the id , we can make a class which acts as a wrapper and allows us to only return the stuff we want it to return 
#to do this:

#the wrapper is then referred to in the decorator as that allows the data whcih will be returned to then be manipulated to conform to the model of the wrapper
class wrapper_data(BaseModel):
    title : str
    class Config():
        orm_mode = True


@app.post("/database_create")
def create_data(request:food , db : Session = Depends(get_db)):
    new_entry = table_one(title = request.potatoes , body = request.steak)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)

    return new_entry

@app.get("/database_retrieval_singular_wrapper" , response_model = wrapper_data)
def get_singular(id , response: Response , db : Session = Depends(get_db)):
    singular_data = db.query(table_one).filter(table_one.id == id).first()#gets all data in the table table_one and then filters the data by finding where the column equals the id and then the first peice of data witht eh id is returned
     #filter() is used to allow data to be found via conditions
    if not singular_data:
        response.status_code = status.HTTP_404_NOT_FOUND
        #to do this a better way and return a comment and have the other stuff retuirn 
        #you use HTTPException 
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail = f"well theres no data with the id {id}")

    return singular_data


