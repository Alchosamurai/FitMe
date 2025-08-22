import os
from dotenv import load_dotenv

load_dotenv("config.env")

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPEN_FOOD_FACTS_URL = "https://world.openfoodfacts.org/cgi/search.pl"