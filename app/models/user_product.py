import datetime
from typing import TYPE_CHECKING
from sqlalchemy import Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.database import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.product import Product


class UserProduct(Base):
    __tablename__ = "user_products"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    amount: Mapped[float] = mapped_column(Float)
    datetime: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.now)
    
    user: Mapped["User"] = relationship("User", back_populates="user_products")
    product: Mapped["Product"] = relationship("Product", back_populates="user_products")
