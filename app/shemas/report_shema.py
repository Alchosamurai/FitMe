from typing import List, Optional
from pydantic import BaseModel, Field
import datetime


class MealToReport(BaseModel):
    title: str = Field(default="")
    calories: int = Field(default=0, ge=0, le=10000, description="Calories of the meal")
    capacity: float = Field(
        default=0, ge=0, le=10000, description="Capacity of the meal"
    )
    protein: int = Field(default=0, ge=0, le=10000, description="Protein of the meal")
    fat: int = Field(default=0, ge=0, le=10000, description="Fat of the meal")
    carbohydrates: int = Field(
        default=0, ge=0, le=10000, description="Carbohydrates of the meal"
    )


class DaysToReport(BaseModel):
    date: datetime.date
    calories: int = Field(default=0, ge=0, le=10000, description="Calories of the day")
    fat: int = Field(default=0, ge=0, le=10000, description="Fat of the day")
    carbohydrates: int = Field(default=0, ge=0, le=10000, description="Carbohydrates of the day")
    protein: int = Field(default=0, ge=0, le=10000, description="Protein of the day")


class BaseReport(BaseModel):
    calories: int
    protein: int
    fat: int
    carbohydrates: int
    target_cal: Optional[int]
    target_protein: Optional[int]
    target_fat: Optional[int]
    target_carbohydrates: Optional[int]
    cal_diff: Optional[int]
    weight_diff: Optional[float]


class DailyReport(BaseReport):
    meals: List[MealToReport]


class RangeReport(BaseReport):
    days: List[DaysToReport]
