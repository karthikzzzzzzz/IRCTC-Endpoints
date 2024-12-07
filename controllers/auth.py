from fastapi import  Depends, APIRouter
from sqlalchemy.orm import Session
from schemas.user import Login, UserTable, BookSeat
from services.users import create_user_details,login_user_details,get_all_trains,booking_seats,get_det
from models import User
from database import get_db
from common.token import get_current_user


app=APIRouter()

@app.post('/create_user')
def create_user(request: UserTable, db: Session = Depends(get_db)):
    return create_user_details(request,db)
    
@app.post('/login_user')
def login_user(request: Login, db: Session = Depends(get_db)):
    return login_user_details(request,db)

@app.get("/get_trains")
def get_trains(source:str,destination:str,db:Session =Depends(get_db)):
    return get_all_trains(source,destination,db)
    
@app.post("/book_seat")
def book_seat(request: BookSeat, db: Session = Depends(get_db)):
    return booking_seats(request, db)
    
@app.get("/get_spec_details/{id}")
def get_specifiy_details(id:int,db:Session=Depends(get_db)):
    return get_det(id,db)
    