from enum import Enum


class UserState(Enum):
    START = "start"
    ADD_PRODUCT = "add_product"
    ADD_PRODUCT_AMOUNT = "add_product_amount"
    ADD_PRODUCT_DATE = "add_product_date"
    ADD_SELF_AGE = "add_self_age"
    ADD_SELF_WEIGHT = "add_self_weight"
    ADD_SELF_ACTIVITY = "add_self_activity"
    ADD_CUSTOM_PRODUCT_NAME = "add_custom_product_name"
    ADD_CUSTOM_PRODUCT_CAL = "add_custom_product_cal"
