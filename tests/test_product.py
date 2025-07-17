from src.product import Product


def test_product(product: Product) -> None:
    assert product.name == "Морковь"
    assert product.description == "Мытая морковь"
    assert product.price == 30.0
    assert product.quantity == 100
