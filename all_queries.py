from fastapi import FastAPI , Depends , status ,Response , HTTPException
from pydantic import BaseModel
from typing import Optional 
import uvicorn 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column , Integer , String , ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from passlib.context import CryptContext
from tables import user_info , posts_table
from database_handling import get_db
from all_schemas import *
from database_handling import Base , sessionlocal, engine
from routers import post as post_router
from routers import user as user_router
from routers import authentication as authentication_router
app = FastAPI()

Base.metadata.create_all(bind = engine )

app.include_router(post_router.router)
app.include_router(user_router.router)
app.include_router(authentication_router.router)

#all this code has been commented as a mroe efficient way to do this has been doen via api routing:

# @app.post("/database_addition", status_code=201, tags=["posts"])
# def create_new_data(request: post, db: Session = Depends(get_db)):
#     new_favourite_character_entry = posts_table(
#         favouritecharacter=request.favouritecharacter,
#         reason=request.reason,
#         rating=request.rating,
#         user_id=request.user_id
#     )
#     db.add(new_favourite_character_entry)
#     db.commit()
#     db.refresh(new_favourite_character_entry)
#     return new_favourite_character_entry


# @app.get("/database_retrieval", tags=["posts"])
# def get_data(response: Response, db: Session = Depends(get_db)):
#     data = db.query(posts_table).all()
#     return data


# @app.get("/database_retrieval_singular", tags=["posts"])
# def get_singular(id, response: Response, db: Session = Depends(get_db)):
#     singular_data = db.query(posts_table).filter(posts_table.id == id).first()
#     if not singular_data:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"well theres no data with the id {id}")
#     return singular_data


# @app.delete("/database_delete{id}", tags=["posts"])
# def data_delete(id, response: Response, db: Session = Depends(get_db)):
#     delete_data = db.query(posts_table).filter(posts_table.id == id)
#     if not delete_data:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"data with id {id} is not found")
#     else:
#         delete_data.delete(synchronize_session=False)
#         db.commit()
#     return delete_data, "has been deleted"


# @app.put("/database_update{id}", tags=["posts"])
# def data_update(id, request: post, response: Response, db: Session = Depends(get_db)):
#     data = db.query(posts_table).filter(posts_table.id == id)
#     if not data.first:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"data with {id} is not found")
#     else:
#         data.update({"title": request.favouritecharacter})
#         db.commit()
#     return "updated"


# @app.get("/posts/{id}", response_model=UserInPost, tags=["posts"])
# def get_post(id: int, db: Session = Depends(get_db)):
#     user = db.query(user_info).filter(user_info.id == id).first()
#     if not user:
#         raise HTTPException(status_code=404, detail=f"Post with id {id} not found")
#     return user


# === USER ENDPOINTS - MOVED TO routers/user.py ===

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# @app.post("/user", response_model=id_hider, tags=["user_handling"])
# def create_user(request: Usernames_passwords, db: Session = Depends(get_db)):
#     hashedpassword = pwd_context.hash(request.password)
#     new_user_info = user_info(
#         name=request.name,
#         DOB=request.DOB,
#         username=request.username,
#         email=request.email,
#         password=hashedpassword
#     )
#     db.add(new_user_info)
#     db.commit()
#     db.refresh(new_user_info)
#     return new_user_info

# @app.get("/user/{id}", response_model=id_hider, tags=["user_handling"])
# def get_user_by_id(id: int, response: Response, db: Session = Depends(get_db)):
#     wanted_userdata = db.query(user_info).filter(user_info.id == id).first()
#     if not wanted_userdata:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} is not valid")
#     else:
#         return wanted_userdata
