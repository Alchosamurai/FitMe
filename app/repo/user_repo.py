from app.models.user import User
from app.database.database import Session


class UserRepo:
    def __init__(self):
        self.session = Session()

    def get_user_by_id(self, user_id: int) -> User | None:
        return self.session.query(User).filter(User.id == user_id).first()

    def create_user(self, user: User) -> User:
        if self.get_user_by_id(user.id):
            return user
        self.session.add(user)
        self.session.commit()
        return user

    def update_user(self, user: User) -> None:
        self.session.commit()
        return

    def delete_user(self, user_id: int) -> None:
        user = self.get_user_by_id(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return
