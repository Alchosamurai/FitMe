from enum import Enum


class UserState(Enum):
    START = "start"
    ADD_PRODUCT = "add_product"
    ADD_PRODUCT_AMOUNT = "add_product_amount"
    ADD_PRODUCT_DATE = "add_product_date"
