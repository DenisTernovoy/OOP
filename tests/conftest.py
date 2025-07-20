import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product() -> Product:
    return Product("Морковь", "Мытая морковь", 30.0, 100)


@pytest.fixture
def category() -> Category:
    return Category("Овощи", "Весовые товары", [Product("Перец", "Красный", 80, 80)])


@pytest.fixture
def json_data() -> list:
    return [
        {
            "name": "Телефоны",
            "description": "Средства связи",
            "products": [
                {"name": "Samsung", "description": "Телефон", "price": 5000.0, "quantity": 100},
            ],
        }
    ]
