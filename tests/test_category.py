from src.category import Category


def test_product(category: Category) -> None:
    assert category.name == "Овощи"
    assert category.description == "Весовые товары"
    assert category.quantity_of_categories == 1
    assert category.quantity_of_products == 1
