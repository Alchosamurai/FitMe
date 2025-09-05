from enum import Enum
from typing import TYPE_CHECKING, Optional
from sqlalchemy import Integer, String, Float, Boolean, Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.user_product import UserProduct


class Activity(Enum):
    LOW = 0
    MEDIUM = 1
    HIGHT = 2


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String)
    age: Mapped[Optional[int]] = mapped_column(Integer)
    gender: Mapped[Optional[bool]] = mapped_column(Boolean)
    weight: Mapped[Optional[float]] = mapped_column(Float)
    height: Mapped[Optional[float]] = mapped_column(Float)
    activity: Mapped[Activity] = mapped_column(SQLEnum(Activity), default=Activity.MEDIUM)
    goal: Mapped[Optional[str]] = mapped_column(String)
    calories: Mapped[Optional[float]] = mapped_column(Float)
    fat: Mapped[Optional[float]] = mapped_column(Float)
    carbohydrates: Mapped[Optional[float]] = mapped_column(Float)
    protein: Mapped[Optional[float]] = mapped_column(Float)
    uuid: Mapped[Optional[str]] = mapped_column(String)
    
    user_products: Mapped[list["UserProduct"]] = relationship("UserProduct", back_populates="user")
