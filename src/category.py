class Category:
    """Класс для описания категорий товаров"""
    unique_goods_count: int = 0
    set_of_categories: set = set()

    def __init__(self, name: str, description: str, goods: list) -> None:
        """
        Конструктор класса
        :param name: название категории
        :param description: описание категории
        :param goods: товары категории
        """
        self.name = name
        self.description = description
        self.__goods = goods
        self.__class__.unique_goods_count = len(set(self.__goods))
        for e in self.__goods:
            if e.name not in self.__class__.set_of_categories:
                self.__class__.set_of_categories.add(e.name)

    @property
    def get_goods(self):
        goods_list: list = []
        for good in self.__goods:
            # yield f'Продукт, {good.price} руб. Остаток: {good.quantity} шт.'
            goods_list.append(f'Продукт, {good.price} руб. Остаток: {good.quantity} шт.')
        return goods_list
