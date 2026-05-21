from fastapi import APIRouter , Response , Depends , HTTPException
import all_schemas , tables , database_handling , oauth2
from typing import List
from repo import post_endpointfunctions as post_end


#api routing allows endpoints to be grouped up together 
#this allows for end points to be grouped up based on topics making it so that not all endpoints 
#are crammed into one big file 


router = APIRouter(
    tags =["posts"],
    prefix = "/post"
) #initialises router 

get_db = database_handling.get_db
Session = database_handling.Session
post_table = tables.posts_table
post = all_schemas.post
UserInPost = all_schemas.UserInPost

#all endpoints in terms of posting 
@router.get("/", response_model = List[post])
def get_data(response : Response , db : Session = Depends(get_db) , current_user : all_schemas.Usernames_passwords = Depends(oauth2.get_current_user)):
    #to get get the data now we need the database session but as well as that we need a user to be logged in 
    #that user would be represented in teh form of the schema in which it depends on if the get_curernt_user function whcih handles the verficiation of the user via jwt token returns true


    data = db.query(post_table).all()
    return data 

@router.post("/" , status_code = 201 )
def create_new_data(request : post , db : Session = Depends(get_db), current_user : all_schemas.Usernames_passwords = Depends(oauth2.get_current_user)):
    new_favourite_character_entry = posts_table(favouritecharacter = request.favouritecharacter, reason = request.reason, rating = request.rating, user_id = request.user_id)
    db.add(new_favourite_character_entry) 
    db.commit() 
    db.refresh(new_favourite_character_entry)
    return new_favourite_character_entry


@router.get("/{id}")
def get_singular(id , response: Response , db : Session = Depends(get_db), current_user : all_schemas.Usernames_passwords = Depends(oauth2.get_current_user)):
    return post_end.get_userby_id(response , id , db)


@router.delete("/{id}")
def data_delete(id , response : Response, db : Session = Depends(get_db), current_user : all_schemas.Usernames_passwords = Depends(oauth2.get_current_user)):
    delete_data = db.query(posts_table).filter(posts_table.id == id)
    if not delete_data:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail = f"data with id {id} is not found")
    else:
        delete_data.delete(synchronize_session = False)
        db.commit()

    return delete_data , "has been deleted"


@router.put("/{id}")
def data_update(id ,request : post,  response : Response , db : Session = Depends(get_db), current_user : all_schemas.Usernames_passwords = Depends(oauth2.get_current_user)):
    data = db.query(posts_table).filter(posts_table.id == id)
    if not data.first:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail = f"data with {id} is not found")
    else:
        data.update({"title" : request.favouritecharacter})
        db.commit()

    return "updated"




