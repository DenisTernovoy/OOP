import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product() -> Product:
    return Product("Морковь", "Мытая морковь", 30.0, 100)


@pytest.fixture
def product1() -> Product:
    return Product("Огурцы", "Луховицкие", 100.0, 50)


@pytest.fixture
def category() -> Category:
    return Category("Овощи", "Весовые товары", [Product("Перец", "Красный", 80, 80)])


@pytest.fixture
def category1() -> Category:
    return Category(
        "Овощи",
        "Весовые товары",
        [
            Product("Перец", "Красный", 80, 80),
            Product("Морковь", "Мытая морковь", 30.0, 100),
            Product("Огурцы", "Луховицкие", 100.0, 50),
        ],
    )


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
