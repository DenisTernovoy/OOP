import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product() -> Product:
    return Product("Морковь", "Мытая морковь", 30.0, 100)


@pytest.fixture
def category() -> Category:
    return Category("Овощи", "Весовые товары", [Product("Морковь", "Мытая морковь", 30, 100)])
