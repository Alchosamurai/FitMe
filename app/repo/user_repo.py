from typing import Optional
from app.models.user_model import UserBase, UserTargetBase
from app.database.database import get_db


class UserRepo:
    def __init__(self):
        self.session = get_db()

    def get_by_id(self, user_id: int) -> UserBase | None:
        return self.session.query(UserBase).filter(UserBase.id == user_id).first()

    def create(self, user: UserBase) -> UserBase:
        if self.get_user_by_id(user.tg_id):
            return user
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, user: UserBase) -> UserBase:
        updated_user = self.session.merge(user)
        self.session.commit()
        return updated_user

    def delete(self, user_id: int) -> None:
        user = self.get_user_by_id(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return
        return

    def get_by_tg_id(self, tg_id: int) -> Optional[UserBase]:
        return self.session.query(UserBase).filter(UserBase.tg_id == tg_id).first()


class UserDailyRepo:
    def __init__(self):
        self.session = get_db()

    def get_by_user_tg_id(self, user_tg_id: int) -> Optional[UserTargetBase]:
        return (
            self.session.query(UserTargetBase)
            .filter(UserTargetBase.user_tg_id == user_tg_id)
            .first()
        )
    def get_by_user_tg_id_or_default(self, user_tg_id: int) -> Optional[UserTargetBase]:
        return (
            self.get_by_user_tg_id(user_tg_id)
            or UserTargetBase(user_tg_id=user_tg_id, target_cal=0, target_protein=0, target_fat=0, target_carbohydrates=0)
        )

    def create(self, user_daily: UserTargetBase) -> UserTargetBase:
        if self.get_by_user_tg_id(user_daily.user_tg_id):
            return user_daily
        self.session.add(user_daily)
        self.session.commit()
        return user_daily

    def update(self, user_daily: UserTargetBase) -> None:
        self.session.commit()
        return

    def delete(self, user_daily_id: int) -> None:
        user_daily = self.get_by_id(user_daily_id)
        if user_daily:
            self.session.delete(user_daily)
            self.session.commit()
            return
        return
