from typing import Any


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

    @classmethod
    def initialize_product(cls, name: str, description: str, price: float, quantity: int) -> Any:
        """Инициализируем новый экземпляр класса (товар) и возвращаем его"""
        return cls(name, description, price, quantity)

    @property
    def get_price(self) -> float:
        """Геттер цены"""
        return self.price

    @get_price.setter
    def get_price(self, new_price: float) -> None:
        """Сеттер цены"""
        if new_price < self.price:
            input_answer = input("Подтвердите цену: y - снизить, n - оставить.").lower()
            if input_answer == 'y':
                self.price = new_price

    @get_price.deleter
    def get_price(self) -> None:
        """Делитер цены"""
        self.price = None
