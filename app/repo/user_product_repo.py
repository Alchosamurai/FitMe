from app.models.user_product import UserProduct
from app.database.database import Session
import datetime


class UserProductRepo:
    def __init__(self):
        self.session = Session()

    def get_user_product_by_id(self, user_product_id: int) -> UserProduct | None:
        return (
            self.session.query(UserProduct)
            .filter(UserProduct.id == user_product_id)
            .first()
        )

    def create_user_product(self, user_product: UserProduct) -> UserProduct:
        if self.get_user_product_by_id(user_product.id):
            return user_product
        self.session.add(user_product)
        self.session.commit()
        return user_product

    def update_user_product(self, user_product: UserProduct) -> None:
        self.session.commit()
        return

    def get_by_user_id_and_date(
        self, user_id: int, date: datetime.date
    ) -> list[UserProduct]:
        return (
            self.session.query(UserProduct)
            .filter(UserProduct.user_id == user_id, UserProduct.date == date)
            .all()
        )

    def get_by_user_id_and_date_range(
        self, user_id: int, start_date: datetime.date, end_date: datetime.date
    ) -> list[UserProduct]:
        return (
            self.session.query(UserProduct)
            .filter(
                UserProduct.user_id == user_id,
                UserProduct.date >= start_date,
                UserProduct.date <= end_date,
            )
            .all()
        )

    def get_by_user_id(self, user_id: int) -> list[UserProduct]:
        return (
            self.session.query(UserProduct).filter(UserProduct.user_id == user_id).all()
        )

    def get_by_product_id(self, product_id: int) -> list[UserProduct]:
        return (
            self.session.query(UserProduct)
            .filter(UserProduct.product_id == product_id)
            .all()
        )
