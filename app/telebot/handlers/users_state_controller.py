from app.telebot.shemas.user_states import UserState


class UsersStateController:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(UsersStateController, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.users_state = {}
        self.user_states = UserState

    def get_user_state(self, user_id: int) -> UserState:
        return self.users_state.get(user_id, self.user_states.START)

    def set_user_state(self, user_id: int, state: UserState) -> None:
        self.users_state[user_id] = state
