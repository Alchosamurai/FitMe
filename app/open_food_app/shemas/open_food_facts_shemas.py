from pydantic import BaseModel
from typing import List

class OpenFoodFactsProduct(BaseModel):
    name: str
    calories: float
    fat: float
    carbohydrates: float
    protein: float

class OpenFoodFactsProductRequest(BaseModel):
    name: str

class OpenFoodFactsProductResponse(BaseModel):
    products: List[OpenFoodFactsProduct]