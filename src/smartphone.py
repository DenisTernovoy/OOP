from src.product import Product


class Smartphone(Product):
    """Дочерний класс от класса Product, реализующий функционал по товару Смартфон"""

    name: str
    description: str
    price: float
    quantity: int
    efficiency: float
    model: str
    memory: float
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: float,
        color: str,
    ) -> None:
        """Конструктор расширенный от материнского класса Product"""

        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
