class Category:
    """Класс, содержащий информацию о категории продуктов: название, описание, список товаров(products)"""

    name: str
    description: str
    products: list

    quantity_of_categories: int = 0
    quantity_of_products: int = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.products = products

        Category.quantity_of_categories += 1
        Category.quantity_of_products += len(products)
