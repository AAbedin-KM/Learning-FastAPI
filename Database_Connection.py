#Connecting to the Database:

#import all needed modules
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column , Integer , String 
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship #used for creating a relationship between two databases (used in real life application of Fastapi)

#to first make a database connection you have to instantiate the engine 
#the engine needs the url to the database and connect_args 
#the engine allows connection to the actual database so u can then interact with it later
SQLALCHAMY_DATABASE_URL = 'sqlite:///./tutorial.db'
engine = create_engine(SQLALCHAMY_DATABASE_URL , connect_args={
                       "check_same_thread": False})

#now you make a session whcih allwos you to interact with the database and add, delete and update data (later in the series)
sessionlocal = sessionmaker(bind = engine , autocommit = False , autoflush = False) 
#auto commit controls if changes to database should be automatically done 
#bind is the actual database 
#autoflush controls if objects sent to database are automatically sent or should be controlled

#then u make the base which acts as the parent class all tables created shoudl inherit from 
#it is the structure of the table such as making new columns and later on declare foreign keys 
Base = declarative_base()

#to actually create the tables so they pop up on tableplus 
Base.metadata.create_all(bind = engine) #instantiates all tables made in the database
