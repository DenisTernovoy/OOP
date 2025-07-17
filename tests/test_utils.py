import json
from unittest.mock import mock_open, patch

from src.utils import read_json_data
from src.category import Category


def test_read_json_data(json_data: list) -> None:

    Category.category_count = 0  # без этого в тестах сохраняется состояние класса, что приводит к AssertionError
    Category.product_count = 0  # без этого в тестах сохраняется состояние класса, что приводит к AssertionError

    with patch("builtins.open", mock_open(read_data=json.dumps(json_data))):
        result = read_json_data("fake_path.json")

        assert result[0].product_count == 1
        assert result[0].category_count == 1
