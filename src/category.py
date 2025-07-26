from src.product import Product


class Category:
    """Класс, содержащий информацию о категории продуктов: название, описание, список товаров(products)"""

    name: str
    description: str
    __products: list

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __len__(self) -> int:
        count = 0
        for i in self.__products:
            count += i.quantity
        return count

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        products_list = [str(product) for product in self.__products]
        return "\n".join(products_list)
