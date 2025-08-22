from sqlalchemy import Column, Integer, String, Float
from app.database.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    weight = Column(Float)
    height = Column(Float)
    activity = Column(String)
    goal = Column(String)
    calories = Column(Float)
    fat = Column(Float)
    carbohydrates = Column(Float)
    protein = Column(Float)
    uuid = Column(String)
