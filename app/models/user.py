from enum import Enum
from sqlalchemy import Column, Integer, String, Float, Boolean, Enum as SQLEnum
from app.database.database import Base

class Activity(Enum):
    LOW = 0
    MEDIUM = 1
    HIGHT = 2

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(Boolean)
    weight = Column(Float)
    height = Column(Float)
    activity = Column(SQLEnum(Activity), default=Activity.MEDIUM)
    goal = Column(String)
    calories = Column(Float)
    fat = Column(Float)
    carbohydrates = Column(Float)
    protein = Column(Float)
    uuid = Column(String)
