from src.product import Product


class Category:
    """Класс, содержащий информацию о категории продуктов: название, описание, список товаров(products)"""

    name: str
    description: str
    products: list

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)


    def add_product(self, product: Product):
        self.__products.append(product)

