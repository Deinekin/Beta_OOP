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
        pass

    product1 = Product(name="Молоко", description="Молочная продукция", price=73, quantity=12)
    product2 = Product(name="Свинина", description="Мясо", price=356, quantity=17)
    product3 = Product(name="Говядина", description="Мясо", price=549.50, quantity=15)
    print(product1.get_price)
    product1.get_price = 1
    print(product1.get_price)
    #del product1.get_price
    print(product1.get_price)
    print(product1) # Вывод для класса Product работает
    print(category) # Вывод для класса Category работает
    print(product2 + product3) # Сложение цен продуктов работает
