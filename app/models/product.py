from sqlalchemy import Column, Integer, String, Float
from app.database.database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    calories = Column(Float)
    fat = Column(Float)
    carbohydrates = Column(Float)
    protein = Column(Float)
    uuid = Column(String)