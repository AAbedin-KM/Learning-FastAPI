from passlib.context import CryptContext
from fastapi import APIRouter , Response , Depends , HTTPException
import all_schemas , tables , database_handling
from typing import List
from repo import user_endpointfunctions as user_end

router = APIRouter(
    tags=["user_handling"],
    prefix = "/user"
)

#when using the router u can make it so that all endpoints which use the path all go under the same 
#tag , this is done above
#as well as this the prefeix for all endpoints which go under the router can also be written into the instanitialising of the router by 
#doing as above , with this now when refering to an endpoint for the path u can now just do / insetad of the full name 
#these are used for convenience and efficiency
#


id_hider = all_schemas.id_hider
get_db = database_handling.get_db
Session = database_handling.Session
Usernames_passwords = all_schemas.Usernames_passwords
user_info =tables.user_info
UserInPost = all_schemas.UserInPost

pwd_context = CryptContext(schemes =["bcrypt"] , deprecated = "auto")
@router.post("/" , response_model = id_hider , )
def create_user(request : Usernames_passwords , db : Session = Depends(get_db)):
    return user_end.create_user( request , db)

#get user info 
@router.get("/{id}" , response_model = id_hider)
def get_user_by_id(id : int , response : Response , db : Session = Depends(get_db)):
    wanted_userdata = db.query(user_info).filter(user_info.id == id).first()
    if not wanted_userdata:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail = f"user with id: {id} is not valid")
    else:
        return wanted_userdata

#gets the posts of that user 
@router.get("/{id}/posts", response_model= UserInPost)     
def get_post(id: int, db: Session = Depends(get_db)):
    user = db.query(user_info).filter(user_info.id == id).first()        
    if not user:
        raise HTTPException(status_code=404, detail=f"Post with id {id} not found")
    return user