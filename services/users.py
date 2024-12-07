from enum import verify
from urllib import request
from fastapi import Depends, HTTPException, status
from database import get_db
from sqlalchemy.orm import Session
from schemas.user import Login, UserTable, BookSeat
import models
from hashing.hash import Hash
from models import Train, User, Book, Token
from common.token import create_access_token, get_current_user



def create_user_details(request: UserTable, db: Session = Depends(get_db)):
    hashed_password = Hash.hash_password(request.password)
    new_user = models.User(
        username=request.username,
        email=request.email,
        password=hashed_password,
        role=request.role,
        id=request.id
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def login_user_details(request: Login, db: Session = Depends(get_db)):
    
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    if not Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Password")
    
    token = create_access_token({"sub": user.id})  
    new_token = Token(token=token, user_id=user.id)
    db.add(new_token)
    db.commit()
    print(f"Token saved to database: {token}") 
    return {"access_token": token}


def get_all_trains(source:str,destination:str,db:Session =Depends(get_db)):
    trains=db.query(Train).filter(Train.source == source,Train.destination == destination).all()
    return [{"train_name":train.train_name, "available_seats":train.available_Seats} for train in trains]

def booking_seats(request: BookSeat, db: Session = Depends(get_db)):

    token = request.token  
    user = get_current_user(token, db)

    train = db.query(Train).filter(Train.id == request.train_id).first()
    if not train:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Train not found")

    if train.available_Seats < request.seats:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Seats not available")

    new_booking = Book(user_id=user.id, train_id=train.id, seats=request.seats)
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)

    return {"message": "Booking successful"}


def get_det(id:int,db:Session=Depends(get_db)):
    booking=db.query(models.Book).filter(models.Book.id==id).first()
    if not booking:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Booking not found")
    return {
        "user_id":booking.user_id,
        "train_id":booking.train_id,
    }