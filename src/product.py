from typing import Any


class Product:
    """Класс для товаров с указанием цены и количества в наличии"""

    product_list: list = []

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

    def __str__(self) -> str:
        """Магический метод для вывода информации"""
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other) -> float | int:
        """Магический метод для сложения общей стоимости двух товаров"""
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def add_product(cls, *args) -> None:
        """Метод, при помощи которого в список продуктов добавляются
        объекты только класса Product или его наследников"""
        if issubclass(cls, Product):
            cls.product_list.append(cls(*args))


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, productivity: float, model: str,
                 memory: int, color: str) -> None:
        """Конструктор класса Smartphone"""
        super().__init__(name, description, price, quantity)
        self.productivity = productivity
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Метод сложения цен объектов только класса Smartphone"""
        if isinstance(self, Smartphone) and isinstance(other, Smartphone):
            return self.price + other.price
        raise TypeError


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, manufacturer_country: str,
                 germination_period: int, color: str):
        """Конструктор класса LawnGrass"""
        super().__init__(name, description, price, quantity)
        self.manufacturer_country = manufacturer_country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Метод сложения цен объектов только класса LawnGrass"""
        if isinstance(self, LawnGrass) and isinstance(other, LawnGrass):
            return self.price + other.price
        raise TypeError
