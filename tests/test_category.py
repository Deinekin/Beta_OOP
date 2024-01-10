import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def category_init():
    product_1 = Product(name='Хлеб', description='Выпечка', price=56.90, quantity=200)
    product_2 = Product(name='Хлеб', description='Выпечка', price=45.90, quantity=54)
    product_3 = Product(name='Молоко', description='Молочные изделия', price=78, quantity=14)
    products_list = [product_1, product_2, product_3]
    category_1 = Category(name='Пятерочка', description='Продовольственный магазин', goods=products_list)
    category_2 = Category(name='Пятерочка', description='Продовольственный магазин', goods=products_list)
    category_3 = Category(name='Перекресток', description='Продовольственный магазин', goods=products_list)
    return [category_1, category_2, category_3]


def test_category_init(category_init):
    assert category_init[0].name == 'Пятерочка'
    assert category_init[1].description == 'Продовольственный магазин'


def test_category_count():
    assert Category.unique_goods_count == 3
    assert len(Category.set_of_categories) == 2
