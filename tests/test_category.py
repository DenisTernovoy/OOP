from typing import Any
from unittest.mock import patch

import pytest

from src.category import Category
from src.product import Product


def test_category(category: Category) -> None:
    assert category.name == "Овощи"
    assert category.description == "Весовые товары"
    assert category.category_count == 1
    assert category.product_count == 1


def test_category_add_product(category: Category, product: Product) -> None:
    product_count = category.product_count
    category.add_product(product)
    assert category.product_count == product_count + 1


@patch("tests.conftest.product")
def test_category_add_product_2(mock_data: Any, category: Category, product: Product) -> None:
    Category.category_count = 0

    mock_data.return_value = "Не продукт"

    with pytest.raises(TypeError):
        category.add_product(mock_data)


def test_category_products(category: Category) -> None:
    assert category.products == "Перец, 80 руб. Остаток: 80 шт."


def test_category_len(category: Category) -> None:
    assert len(category) == 80


def test_category_str(category: Category) -> None:
    assert str(category) == "Овощи, количество продуктов: 80 шт."


def test_category_invalid() -> None:
    cat1 = Category("Телефоны", "Мобильные", [])
    assert cat1.middle_price() == 0


def test_category_middle_price(category1: Category) -> None:
    assert category1.middle_price() == 70.0
