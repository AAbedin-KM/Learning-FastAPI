from fastapi import APIRouter , Depends , HTTPException , status  
import all_schemas , tables , database_handling
import repo.authentication_endpointfunctions as authentication_end
from fastapi.security import OAuth2PasswordRequestForm



router = APIRouter(
    tags=["Authentication"] , 
    prefix = "/Authentication"
)

login = all_schemas.login
get_db = database_handling.get_db
Session = database_handling.Session
userinfo = tables.user_info 

@router.post("/login")
def login(request : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)):
    return authentication_end.login(request , db) #the function refers to the repo folder which contains a a file where the actual function is written 


    
