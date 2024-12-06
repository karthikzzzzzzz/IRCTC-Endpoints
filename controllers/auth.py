from fastapi import  Depends, APIRouter
from sqlalchemy.orm import Session
from schemas.user import UserTable
from services.users import create_user_details

from database import get_db



app=APIRouter()




@app.post('/user')
def create_user(request: UserTable, db: Session = Depends(get_db)):
    return create_user_details(request,db)
    