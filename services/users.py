from fastapi import Depends, HTTPException, status
from database import get_db
from sqlalchemy.orm import Session
from schemas.user import UserTable
import models
from hashing.hash import Hash


def create_user_details(request: UserTable, db: Session = Depends(get_db)):
    hashed_password = Hash.hash_password(request.password)
    new_user = models.User(
        username=request.username,
        email=request.email,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

