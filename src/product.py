class Product:
    """Класс для товаров с указанием цены и количества в наличии"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """
        Конструктор класса
        :param name: название продукта
        :param description: описание продукта
        :param price: цена продукта
        :param quantity: количество продукта
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
