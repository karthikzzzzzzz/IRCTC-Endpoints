from fastapi import  FastAPI
import models
from database import engine
from controllers import auth

app=FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(auth.app, tags=['Login'])