from typing import TYPE_CHECKING, Optional
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.user_product import UserProduct


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(40))
    calories: Mapped[Optional[float]] = mapped_column(Float())
    fat: Mapped[Optional[float]] = mapped_column(Float)
    carbohydrates: Mapped[Optional[float]] = mapped_column(Float)
    protein: Mapped[Optional[float]] = mapped_column(Float)
    uuid: Mapped[Optional[str]] = mapped_column(String)

    user_products: Mapped[list["UserProduct"]] = relationship("UserProduct", back_populates="product")
