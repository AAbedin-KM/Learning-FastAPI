from fastapi import FastAPI 
from pydantic import BaseModel
from typing import Optional 
from database_handling import Base
import uvicorn 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column , Integer , String , ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from passlib.context import CryptContext

class user_info(Base): #extend the data base by adding another table 
    __tablename__ = "Usernames + Passwords"
    id = Column(Integer , primary_key = True , index = True)
    name = Column(String)
    username = Column(String)
    DOB = Column(String)
    email = Column(String)
    password = Column(String) 
    posts = relationship("posts_table" , back_populates= "userinfo") #creates an point to where the post table connects to to create link


class posts_table(Base):
    __tablename__ = 'Posts' #the name of the table must be set 
    id = Column(Integer , primary_key = True  , index = True) #makes a column called id and makes that column the primary key
    user_id =  Column(Integer , ForeignKey("Usernames + Passwords.id")  , index = True)
    favouritecharacter = Column(String) #make a column called " [what u enter]"
    reason = Column(String) #makle a column called " [what u enter]"
    rating = Column(Integer)
    userinfo = relationship("user_info" , back_populates = "posts" ) #creates a point to where the user info table connects to 
    

#relationships : what i have learnt after debugging:
#figure out what info u want to repsent in what order
#make a schema to actually strcutre the output 
#in it where there are many to many links you make a variable and then have it equaL TO A list[schema for one thing] = []
#this allows multiple schemas with data filled in to be presented item by item 
#for this to work you have to make a foreign key on the many side table and explicitly say it has to conect to a attribute in the one side
#eg user_id = Column(Integer , ForeignKey("Usernames + Passwords.id"))
#this allows the values stoed iun the user_id column  to be used to link to the values of id on the usernamepassword table 
#this connects the two tables 
#with this you can now use relationships 
#when using this make sure the variables of the schema which refer to the many side are teh same as in the many side table 
#eg in my code i want to display all the posts of a user
#so I say posts : list[post] = []
#so all the variables in post such as reason and favourite charcater have to now be the exact same as the columns in the posts table 
#you have to make sure everything is constant 
