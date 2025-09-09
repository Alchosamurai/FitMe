from app.models.user_model import Activity


class CalculateCPFC:
    def __init__(
        self, weight: float, height: float, age: int, gender: bool, activity: Activity
    ):
        self.gender = gender
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender
        self.activity = activity
        self.calories = self.calculate_calories()
        self.protein = self.calculate_protein()
        self.fat = self.calculate_fat()
        self.carbohydrates = self.calculate_carbohydrates()

    def calculate_calories(self) -> float:
        return (
            10 * self.weight + 6.25 * self.height - 5 * self.age + 5
            if self.gender == 0
            else 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
        )

    def calculate_protein(self) -> float:
        return self.weight * self.activity.value

    def calculate_fat(self) -> float:
        return self.calories * 0.25

    def calculate_carbohydrates(self) -> float:
        return (self.calories * 0.5) / 4


class CalculateWeight:
    @staticmethod
    def calories_to_weight(calories: float) -> float:
        return calories / 7700
