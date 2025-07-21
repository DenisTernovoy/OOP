import pytest

from src.category import Category
from src.iterator import CategoryIterator


def test_category_iterator(category1: Category) -> None:
    iterator = CategoryIterator(category1)
    assert iterator.index == -1
    assert iterator.__iter__() == iterator
    assert next(iterator).name == "Перец"
    assert next(iterator).name == "Морковь"
    assert next(iterator).name == "Огурцы"

    with pytest.raises(StopIteration):
        next(iterator)
