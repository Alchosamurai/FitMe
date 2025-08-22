from pydantic import BaseModel
from typing import List


class OpenFoodFactsProduct(BaseModel):
    name: str
    calories: float
    fat: float
    carbohydrates: float
    protein: float
    uuid: str

    def __str__(self):
        return f"{self.name} - {self.calories} ккал/100г"

    def to_callback(self) -> str:
        return f"product_{{name={self.name}, uuid={self.uuid}, calories={self.calories}, fat={self.fat}, carbohydrates={self.carbohydrates}, protein={self.protein}}}"


class OpenFoodFactsProductRequest(BaseModel):
    name: str


class OpenFoodFactsProductResponse(BaseModel):
    products: List[OpenFoodFactsProduct]
