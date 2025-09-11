from typing import Optional
from enum import Enum
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base_model import Base


class Activity(Enum):
    LOW = 0.8
    MEDIUM = 1.5
    HIGH = 2.2


class UserBase(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(unique=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(40))
    age: Mapped[Optional[int]]
    gender: Mapped[Optional[bool]]
    weight: Mapped[Optional[float]]
    height: Mapped[Optional[float]]
    activity: Mapped[Activity] = mapped_column(default=Activity.MEDIUM)
    target: Mapped[Optional["UserTargetBase"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )


class UserTargetBase(Base):
    __tablename__ = "user_daily"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_tg_id: Mapped[int] = mapped_column(ForeignKey("user.tg_id"))
    user: Mapped["UserBase"] = relationship(back_populates="addresses")
    target_cal: Mapped[Optional[int]]
    target_protein: Mapped[Optional[int]]
    target_fat: Mapped[Optional[int]]
    target_carbohydrates: Mapped[Optional[int]]
