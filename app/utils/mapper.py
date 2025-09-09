from app.models.meal_model import MealBase
from app.shemas.report_shema import MealToReport


class MealMapper:
    @staticmethod
    def meal_to_report(meal: MealBase) -> MealToReport:
        return MealToReport(
            title=meal.title,
            capacity=meal.capacity,
            cal=meal.cal,
            protein=meal.protein,
            fat=meal.fat,
            carbohydrates=meal.carbohydrates,
        )
