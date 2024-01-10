from src.category import Category
from src.product import Product

if __name__ == '__main__':
    products_list: list = [
        Product.initialize_product(name="Молоко", description="Молочная продукция", price=73, quantity=12),
        Product.initialize_product(name="Свинина", description="Мясо", price=356, quantity=17),
        Product.initialize_product(name="Молоко", description="Молочная продукция", price=73.50, quantity=120)]

    category = Category(name='Пятерочка', description='Продовольственный магазин', goods=products_list)
    # print(*category.get_goods)
    for e in category.get_goods:
        print(e)

    product = Product(name="Молоко", description="Молочная продукция", price=73, quantity=12)
    print(product.get_price)
    product.get_price = 1
    print(product.get_price)
    del product.get_price
    print(product.get_price)
