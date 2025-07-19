from typing import Any


class Product:
    """Класс, содержащий информацию о продукте: название, описание, цена и количество"""

    name: str
    description: str
    price: float
    quantity: int

    __list_of_products: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        Product.__list_of_products.append(self.__dict__)

    @classmethod
    def new_product(cls, dict_data: dict) -> Any:
        for i in cls.__list_of_products:
            if dict_data["name"] == i["name"]:
                if dict_data["price"] > i["price"]:
                    i["price"] = dict_data["price"]
                i["quantity"] += dict_data["quantity"]

                return None

        return Product(**dict_data)
