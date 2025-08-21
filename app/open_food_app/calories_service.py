import aiohttp
import asyncio
import ssl
from typing import List
from shemas.open_food_facts_shemas import OpenFoodFactsProduct
from pprint import pprint

class CaloriesService:
    def __init__(self):
        self.base_url = "https://world.openfoodfacts.org/cgi/search.pl"
        self.json_param = 1
        self.search_simple_param = 1
        self.action_param = "process"
        self.page_size_param = 10
        self.search_terms_param = ""
        
    def _get_params(self) -> dict:
        return {
            "json": self.json_param,
            "search_simple": self.search_simple_param,
            "action": self.action_param,
            "page_size": self.page_size_param,
            "search_terms": self.search_terms_param
        }

    def _get_ssl_context(self) -> ssl.SSLContext:
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        return ssl_context
    
    async def get_calories_by_name(self, name: str) -> List[OpenFoodFactsProduct] | None:
        self.search_terms_param = name
        params = self._get_params()
        ssl_context = self._get_ssl_context()
        connector = aiohttp.TCPConnector(ssl=ssl_context)
        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.get(self.base_url, params=params) as response:
                data = await response.json()
                products = data["products"]
                if len(products) == 0:
                    return None
                products_list = []
                for product in products:
                    product = OpenFoodFactsProduct(
                        name=product["product_name"],
                        calories=float(product["nutriments"]["energy-kcal_100g"]),
                        fat=product["nutriments"].get("fat_100g", 0),
                        carbohydrates=product["nutriments"].get("carbohydrates_100g", 0),
                        protein=product["nutriments"].get("proteins_100g", 0),
                    )
                    products_list.append(product)
                return products_list

async def main():
    service = CaloriesService()
    result = await service.get_calories_by_name("пицца")
    pprint(f"Калории для 'пицца': {result}")

if __name__ == "__main__":
    asyncio.run(main())