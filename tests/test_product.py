import pytest
from src.product import Product


@pytest.fixture
def product_init():
    return Product(name='Хлеб', description='Выпечка', price=56.90, quantity=200)


def test_product_init(product_init):
    assert product_init.name == 'Хлеб'
    assert product_init.description == 'Выпечка'
    assert product_init.price == 56.90
    assert product_init.quantity == 200
