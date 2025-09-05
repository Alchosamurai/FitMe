import datetime
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.models.user import User
from sqlalchemy.orm import relationship
from app.models.base_model import Base


class Meal(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_tg_id: Mapped[int] = mapped_column(ForeignKey("user.tg_id"))
    user: Mapped["User"] = relationship("User", back_populates="meals")
    title: Mapped[str] = mapped_column(String(100))
    capacity: Mapped[float]
    cal: Mapped[int]
    protein: Mapped[int]
    fat: Mapped[int]
    carbohydrates: Mapped[int]
    timestamp: Mapped[datetime.datetime]




