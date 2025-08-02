import pytest

from src.order import Order
from src.product import Product


def test_order(product: Product) -> None:
    order = Order(product, 10)
    assert order.name == "Морковь"
    assert order.quantity == 10
    assert order.price == 300.0


def test_order_invalid(product: Product) -> None:

    with pytest.raises(ValueError):
        Order(product, 101)
