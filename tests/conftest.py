import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


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


@pytest.fixture
def smartphone() -> Smartphone:
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def lawngrass() -> LawnGrass:
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
