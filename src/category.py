class Category:
    """Класс для описания категорий товаров"""
    unique_goods: int = 0
    quantity_of_categories: set = set()

    def __init__(self, name: str, description: str, goods: list) -> None:
        """
        Конструктор класса
        :param name: название категории
        :param description: описание категории
        :param goods: товары категории
        """
        self.name = name
        self.description = description
        self.goods = goods
        self.__class__.unique_goods = len(set(self.goods))
        if self.name not in self.__class__.quantity_of_categories:
            self.__class__.quantity_of_categories.add(self.name)



