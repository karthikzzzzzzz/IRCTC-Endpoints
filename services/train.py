from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Train
from schemas.user import TrainModel

ADMIN_API_KEY = "admin@123"

def create_train(request: TrainModel, apikey: str, db: Session):
    if apikey == ADMIN_API_KEY:
        
        new_train = Train(
            train_name=request.train_name,
            source=request.source,
            destination=request.destination,
            available_Seats=request.available_seat,
            total_seats=request.tot_seat
        )
       
        db.add(new_train)
        db.commit()
        db.refresh(new_train)
        return new_train
    else:
        raise HTTPException(status_code=403, detail="You are not authorized to add train")
