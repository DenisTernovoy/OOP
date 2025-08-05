from typing import Any

from src.base_order_category import BaseOrderCategory


def test_base_order_category() -> None:
    class Test(BaseOrderCategory):

        def add_product(self, *args: Any, **kwargs: Any) -> Any:
            pass

    test = Test()

    BaseOrderCategory.add_product(test)
