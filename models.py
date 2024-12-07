from database import Base
from sqlalchemy import Column,Integer,String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
    

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True,index=True)
    password=Column(String)
    email=Column(String)
    role=Column(String)
    tokens = relationship("Token", back_populates="user")

class Train(Base):
    __tablename__='train'
    id=Column(Integer,primary_key=True,index=True)
    train_name=Column(String)
    total_seats=Column(Integer)
    available_Seats=Column(Integer)
    source=Column(String)
    destination=Column(String)

class Book(Base):
    __tablename__="book"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"))
    train_id=Column(Integer,ForeignKey("train.id"))
    seats=Column(Integer)
    time=Column(String)
    user=relationship("User")
    train=relationship("Train")

class Token(Base):
    __tablename__ = 'tokens'

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='tokens')    
        