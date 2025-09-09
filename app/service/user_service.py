import datetime
from collections import defaultdict
from app.repo.meal_repo import MealRepo
from app.repo.user_repo import UserRepo, UserDailyRepo
from app.models.user_model import UserBase, UserTargetBase
from app.models.meal_model import MealBase
from app.shemas.report_shema import DailyReport, RangeReport, MealToReport, DaysToReport
from app.utils.formulas import CalculateCPFC, CalculateWeight
from app.utils.mapper import MealMapper


class UserService:
    def __init__(self):
        self.user_repo = UserRepo()
        self.meal_repo = MealRepo()
        self.user_daily_repo = UserDailyRepo()
        self.meal_mapper = MealMapper()

    def get_user_by_id(self, user_id: int) -> UserBase:
        return self.user_repo.get_by_id(user_id)

    def create_user(self, user: UserBase) -> UserBase:
        return self.user_repo.create(user)

    def update_user(self, user: UserBase) -> UserBase:
        return self.user_repo.update(user)

    def delete_user(self, user_id: int) -> None:
        return self.user_repo.delete(user_id)

    def get_today_meals(self, user_id: int) -> list[MealBase]:
        return self.meal_repo.get_by_user_tg_id_and_date(user_id, datetime.date.today())

    def get_range_report_by_tg_id(
        self, user_tg_id: int, start_date: datetime.date, end_date: datetime.date
    ) -> RangeReport:
        target = self.user_daily_repo.get_by_user_tg_id_or_default(user_tg_id)
        meals = self.meal_repo.get_by_user_tg_id_and_date_range(
            user_tg_id, start_date, end_date
        )
        meals_by_date = defaultdict(DaysToReport())

        for meal in meals:
            meals_by_date[meal.date.day].calories += meal.cal
            meals_by_date[meal.date.day].protein += meal.protein
            meals_by_date[meal.date.day].fat += meal.fat
            meals_by_date[meal.date.day].carbohydrates += meal.carbohydrates

        days = len(meals_by_date)
        target_cal = target.target_cal * days
        target_protein = target.target_protein * days
        target_fat = target.target_fat * days
        target_carbohydrates = target.target_carbohydrates * days

        cal_diff = target_cal - sum(meal.calories for meal in meals_by_date.values())
        weight_diff = CalculateWeight.calories_to_weight(cal_diff)

        return RangeReport(
            target_cal=target_cal,
            target_protein=target_protein,
            target_fat=target_fat,
            target_carbohydrates=target_carbohydrates,
            days=list(meals_by_date.values()),
            calories=sum(meal.calories for meal in meals_by_date.values()),
            protein=sum(meal.protein for meal in meals_by_date.values()),
            fat=sum(meal.fat for meal in meals_by_date.values()),
            carbohydrates=sum(meal.carbohydrates for meal in meals_by_date.values()),
            cal_diff=cal_diff,
            weight_diff=weight_diff,
        )

    def get_today_report(self, user_id: int) -> DailyReport:
        meals = self.meal_repo.get_by_user_tg_id_and_date(
            user_id, datetime.date.today()
        )
        target = self.user_daily_repo.get_by_user_tg_id_or_default(user_id)
        meals = [self.meal_mapper.meal_to_report(meal) for meal in meals]
        cal_diff = target.target_cal - sum(meal.calories for meal in meals)
        weight_diff = CalculateWeight.calories_to_weight(cal_diff)
        return DailyReport(
            target_cal=target.target_cal,
            target_protein=target.target_protein,
            target_fat=target.target_fat,
            target_carbohydrates=target.target_carbohydrates,
            meals=meals,
            calories=sum(meal.calories for meal in meals),
            protein=sum(meal.protein for meal in meals),
            fat=sum(meal.fat for meal in meals),
            carbohydrates=sum(meal.carbohydrates for meal in meals),
            cal_diff=cal_diff,
            weight_diff=weight_diff,
        )

    def get_month_report(self, user_id: int, month: datetime.month) -> RangeReport:
        pass
