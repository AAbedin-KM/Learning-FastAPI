from fastapi import APIRouter , Response , Depends , HTTPException , status 
import all_schemas , tables , database_handling
from typing import List



Session = database_handling.Session
posts_table = tables.posts_table
post = all_schemas.post


def get_userby_id(response ,  id : int , db: Session  ):
    singular_data = db.query(posts_table).filter(posts_table.id == id).first()
    if not singular_data:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND , detail = f"well theres no data with the id {id}")
    return singular_data