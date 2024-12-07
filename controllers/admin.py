from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.user import TrainModel
from services.train import create_train
from database import get_db

app = APIRouter()

@app.post('/add_train/{apikey}')
def add_train(request: TrainModel, apikey: str, db: Session = Depends(get_db)):
    return create_train(request=request, apikey=apikey, db=db)
