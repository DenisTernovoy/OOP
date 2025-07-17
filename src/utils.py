import json

from src.category import Category
from src.product import Product


def read_json_data(path: str) -> list[Category]:
    """Функция осуществляет подгрузку данных по категориям и товарам из файла JSON"""

    list_of_categories = []

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    for category in data:
        product_list = []
        for product in category["products"]:
            product_list.append(Product(**product))
        category["products"] = product_list
        list_of_categories.append(Category(**category))

    return list_of_categories
