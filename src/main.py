from src.category import Category
from src.product import Product, Smartphone, LawnGrass

if __name__ == '__main__':
    products_list: list = [
        Product.initialize_product(name="Молоко", description="Молочная продукция", price=73, quantity=12),
        Product.initialize_product(name="Свинина", description="Мясо", price=356, quantity=17),
        Product.initialize_product(name="Молоко", description="Молочная продукция", price=73.50, quantity=120)]

    category = Category(name='Пятерочка', description='Продовольственный магазин', goods=products_list)
    category1 = Category(name='Пятерочка', description='Продовольственный магазин', goods=[])
    # print(*category.get_goods)
    for e in category.get_goods:
        print(e)
        pass

    product1 = Product(name="Молоко", description="Молочная продукция", price=73, quantity=12)
    product2 = Product(name="Свинина", description="Мясо", price=356, quantity=17)
    product3 = Product(name="Говядина", description="Мясо", price=549.50, quantity=15)
    print(product1.get_price)
    # product1.get_price = 1
    print(product1.get_price)
    # del product1.get_price
    print(product1.get_price)
    print(product1)  # Вывод для класса Product работает
    print(category)  # Вывод для класса Category работает
    print(product2 + product3)  # Сложение цен продуктов работает

    smartphone1 = Smartphone(name="Xiaomi", description="smartphone", price=15000, quantity=24, productivity=87.8,
                             model="Redmi Note 9", memory=256, color="blue")
    smartphone2 = Smartphone(name="Xiaomi", description="smartphone", price=18000, quantity=5, productivity=87.8,
                             model="Redmi Note 9", memory=512, color="blue")
    lawn_grass1 = LawnGrass(name="Трава газонная", description="хорошая трава", price=5000.0, quantity=2,
                            manufacturer_country="Голландия",
                            germination_period=6, color="green")
    lawn_grass2 = LawnGrass(name="Трава газонная", description="трава похуже", price=0.01, quantity=100000,
                            manufacturer_country="Албания",
                            germination_period=1, color="brown")

    print(lawn_grass2 + lawn_grass1)
    print(f"{type(product1)} {type(smartphone1)} {type(lawn_grass1)}")

    smartphone1.add_product("Xiaomi", "smartphone", 18000, 5, 87.8, "Redmi Note 9", 512, "blue")

    for e in smartphone1.product_list:
        print(e)

    print(repr(smartphone1))
    print(repr(product1))
    print(repr(lawn_grass2))
    print(category.avg_price()) # средняя цена норм работает
    print(category1.avg_price()) # средней цены нет из-за деления на 0, ZeroDivisionError
    smartphone5 = Smartphone(name="Xiaomi", description="smartphone", price=15000, quantity=0, productivity=87.8,
                             model="Redmi Note 9", memory=256,
                             color="blue")  # Ошибка с добавлением нулевого количества товаров, программа дропается
