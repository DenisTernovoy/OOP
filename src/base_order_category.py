from abc import ABC, abstractmethod
from typing import Any


class BaseOrderCategory(ABC):
    """Базовый абстрактный класс, являющийся родительским для классов Order и Category"""

    @abstractmethod
    def add_product(self, *args: Any, **kwargs: Any) -> Any:
        pass
