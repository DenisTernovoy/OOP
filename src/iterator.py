from typing import Any

from src.category import Category
from src.product import Product


class CategoryIterator:
    """
    Вспомогательный класс, с помощью которого можно перебирать товары одной категории, например в цикле for.
    """

    def __init__(self, category: Category):
        self.category = category
        self.index = -1

    def __iter__(self) -> Any:
        return self

    def __next__(self) -> Any:
        if self.index < len(self.category.__dict__["_Category__products"]) - 1:
            self.index += 1
            return self.category.__dict__["_Category__products"][self.index]
        else:
            raise StopIteration
