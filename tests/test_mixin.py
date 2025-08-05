from typing import Any

from src.product import Product


def test_mixin(capsys: Any) -> None:
    Product("Морковь", "Мытая морковь", 30.0, 100)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(Морковь, Мытая морковь, 30.0, 100)"
