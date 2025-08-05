from typing import Any

from src.base_product import BaseProduct
from src.mixin import Mixin


class Product(Mixin, BaseProduct):
    """Класс, содержащий информацию о продукте: название, описание, цена и количество"""

    name: str
    description: str
    __price: float
    quantity: int

    __list_of_products: list = []

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        Product.__list_of_products.append(self.__dict__)
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        if type(self) is type(other):
            return self.__price * self.quantity + other.__price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, dict_data: dict) -> Any:
        for i in cls.__list_of_products:
            if dict_data["name"] == i["name"]:
                if dict_data["price"] > i["_Product__price"]:
                    i["_Product__price"] = dict_data["price"]
                i["quantity"] += dict_data["quantity"]

                return None

        return Product(**dict_data)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            user_input = input("Подтвердите, что цена понижается (y/n): ").lower().strip()
            if user_input == "y":
                self.__price = new_price
        else:
            self.__price = new_price
