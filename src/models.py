import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    dateSubscription = Column(DateTime, nullable=False)
    name = Column(String(200), nullable=False)
    lastName = Column(String(200), nullable=False)
    phone = Column(String(20), nullable=False)   
    favorites = relationship('Favorite', backref='user', lazy=True) 

    def __repr__(self):
        return '<User %r>' % self.name

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    population = Column(Integer, nullable=False)
    rotationPeriod = Column(Integer, nullable=False)
    orbitalPeriod = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    gravity = Column(Integer, nullable=False)
    terrain = Column(String(120), nullable=False)
    surfaceWater = Column(Integer, nullable=False)
    climate = Column(String(120), nullable=False)
    characters = relationship('Character', backref='planet', lazy=True)
    favorites = relationship('Favorites', backref='planet', lazy=True)


    def __repr__(self):
        return '<Planet %r>' % self.name
    
class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    model = Column(String(120), nullable=False)
    manufacturer = Column(String(120), nullable=False)
    classVehicle = Column(String(120), nullable=False)
    cost = Column(Integer, nullable=False)
    speed = Column(Integer, nullable=False)
    length = Column(Float(120), nullable=False)
    cargoCapacity = Column(Integer, nullable=False)
    mimimumCrew = Column(Integer, nullable=False)
    passengers = Column(Integer, nullable=False)
    favorites = relationship('Favorites', backref='vehicle', lazy=True)

    def __repr__(self):
        return '<Vehicle %r>' % self.name
    
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(Integer, nullable=False) 
    species = Column(String(250), nullable=False)
    height = Column(Float(120), nullable=False)
    mass = Column(Integer, nullable=False)
    gender = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)
    favorites = relationship('Favorites', backref='character', lazy=True)
    
    def __repr__(self):
        return '<Character: %r>' % self.name
    
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
