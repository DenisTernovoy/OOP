from src.base_order_category import BaseOrderCategory
from src.product import Product


class Order(BaseOrderCategory):
    """Класс, содержащий информацию о купленном товаре"""

    name: str
    quantity: int
    price: float

    def __init__(self, product: Product, quantity: int) -> None:
        self.name = product.name
        self.quantity = quantity
        self.price = self.add_product(product)

    def add_product(self, product: Product) -> float:
        if self.quantity > product.quantity:
            raise ValueError("Недостаточно товара на складе")
        return self.quantity * product.price
