from app.models.meal_model import MealBase
from app.database.database import get_db
import datetime


class MealRepo:
    def __init__(self):
        self.session = get_db()

    def get_by_id(self, meal_id: int) -> MealBase | None:
        return self.session.query(MealBase).filter(MealBase.id == meal_id).first()

    def create(self, meal: MealBase) -> MealBase:
        self.session.add(meal)
        self.session.commit()
        return meal

    def update(self, meal: MealBase) -> None:
        self.session.commit()
        return

    def delete(self, meal_id: int) -> None:
        meal = self.get_by_id(meal_id)
        if meal:
            self.session.delete(meal)
            self.session.commit()
            return
        return

    def get_by_user_tg_id(self, user_tg_id: int) -> list[MealBase]:
        return (
            self.session.query(MealBase).filter(MealBase.user_tg_id == user_tg_id).all()
        )

    def get_by_user_tg_id_and_date(
        self, user_tg_id: int, date: datetime.date
    ) -> list[MealBase]:
        return (
            self.session.query(MealBase)
            .filter(MealBase.user_tg_id == user_tg_id, MealBase.date == date)
            .all()
        )

    def get_by_user_tg_id_and_date_range(
        self, user_tg_id: int, start_date: datetime.date, end_date: datetime.date
    ) -> list[MealBase]:
        return (
            self.session.query(MealBase)
            .filter(
                MealBase.user_tg_id == user_tg_id,
                MealBase.date >= start_date,
                MealBase.date <= end_date,
            )
            .all()
        )

    def get_by_user_tg_id_and_month(
        self, user_tg_id: int, month: datetime.month
    ) -> list[MealBase]:
        return (
            self.session.query(MealBase)
            .filter(MealBase.user_tg_id == user_tg_id, MealBase.date.month == month)
            .all()
        )
