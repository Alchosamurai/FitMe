import datetime
from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from app.database.database import Base


class UserProduct(Base):
    __tablename__ = "user_products"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    amount = Column(Float) # в граммах
    user = relationship("User", back_populates="user_products")
    product = relationship("Product", back_populates="user_products")
    datetime = Column(DateTime, default=datetime.datetime.now)
