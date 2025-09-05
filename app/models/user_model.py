from typing import Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base_model import Base

class UserBase(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(unique=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(40))
    age: Mapped[Optional[int]]
    weight: Mapped[Optional[float]]
    height: Mapped[Optional[float]]
    target: Mapped["UserDailyBase"] = relationship(back_populates="user", cascade="all, delete-orphan")

class UserDailyBase(Base):
    __tablename__ = 'user_daily'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_tg_id: Mapped[int] = mapped_column(ForeignKey("user.tg_id"))
    user: Mapped["UserBase"] = relationship(back_populates="addresses")
    daily_cal: Mapped[Optional[int]]
    daily_protein: Mapped[Optional[int]]
    daily_fat: Mapped[Optional[int]]
    daily_carbohydrates: Mapped[Optional[int]]
