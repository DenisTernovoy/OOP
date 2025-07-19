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


def test_category_products(category: Category) -> None:
    assert category.products == "Перец, 80 руб. Остаток: 80 шт.\n"
