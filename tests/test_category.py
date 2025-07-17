from src.category import Category


def test_category(category: Category) -> None:
    assert category.name == "Овощи"
    assert category.description == "Весовые товары"
    assert category.category_count == 1
    assert category.product_count == 1
