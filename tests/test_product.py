from typing import Any
from unittest.mock import patch

import pytest

from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_product(product: Product) -> None:
    assert product.name == "Морковь"
    assert product.description == "Мытая морковь"
    assert product.price == 30.0
    assert product.quantity == 100


def test_product_new_product(product: Product) -> None:
    product_count = len(Product.__dict__["_Product__list_of_products"])
    Product.new_product({"name": "Морковь", "description": "Мытая морковь", "price": 60, "quantity": 50})
    assert len(Product.__dict__["_Product__list_of_products"]) == product_count


def test_product_new_product_new(product: Product) -> None:
    product_count = len(Product.__dict__["_Product__list_of_products"])
    Product.new_product({"name": "Лук", "description": "Сушеный", "price": 20, "quantity": 80})
    assert len(Product.__dict__["_Product__list_of_products"]) == product_count + 1


def test_product_price(capsys: Any, product: Product) -> None:
    product.price = -100
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"


def test_product_price_2(product: Product) -> None:
    product.price = 100
    assert product.price == 100


def test_product_price_3(product: Product) -> None:
    with patch("builtins.input", return_value="y"):
        product.price = 10

    assert product.price == 10


def test_product_add(product: Product, product1: Product) -> None:
    res = product + product1
    assert res == 8000


def test_product_add_2(smartphone: Smartphone, lawngrass: LawnGrass) -> None:

    with pytest.raises(TypeError):
        smartphone + lawngrass
