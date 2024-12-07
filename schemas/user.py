from pydantic import BaseModel

class UserTable(BaseModel):
    id:int
    email: str
    password: str
    username: str
    role: str

class Login(BaseModel):
    username: str
    password: str
        
class TrainModel(BaseModel):
    train_name:str 
    source:str
    destination:str
    available_seat:int 
    tot_seat:int      

class BookSeat(BaseModel):
    train_id:int
    seats:int
    token: str 
       