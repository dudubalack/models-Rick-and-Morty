import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    last_surname = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False)
    password = Column(String(12), nullable=False)
    favorite = relationship("Favorite")

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(30),nullable=False)
    status = Column(String(30),nullable=False)
    species = Column(String(30), nullable=False)
    character_type = Column(String(30))
    favorite = relationship("Favorite")
    
class Location(Base):
    __tablename__='location'   
    id = Column(Integer,primary_key=True)
    name = Column(String(120))
    location_type =Column(String(120))
    dimesion = Column(String(120))
    favorite = relationship("Favorite")

class Episode(Base):
    __tablename__='episode'
    id = Column(Integer,primary_key=True)
    name = Column(String(120))
    air_date = Column(DateTime)
    air_date = Column(String(120))
    favorite = relationship("Favorite")

class Favorite(Base):
    __tablename__='favorite'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey("users.id"))
    character_id = Column(Integer, ForeignKey("character.id"))
    location_id = Column(Integer, ForeignKey("location.id"))
    episode_id = Column(Integer, ForeignKey("episode.id"))








    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e


    