"""
Write the programm that calculate total price with discount by the products.

Use class Product(name, price, count) and class Cart. In class Cart you can add the products.

Discount depends on count product:


count	discount
at least 5	5%
at least 7	10%
at least 10	20%
at least 20	30%
more than 20	50%
Write unittest with class CartTest and test all methods with logic
"""


import unittest

class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


class Cart:
    def __init__(self, products_list):
        self.products_list = products_list
    
    @staticmethod
    def calculate_discount(count_discount):
        if count_discount > 20:
            return 0.5
        elif count_discount >= 20:
            return 0.7
        elif count_discount >= 10:
            return 0.8
        elif count_discount >= 7:
            return 0.9
        elif count_discount >= 5:
            return 0.95
        else:
            return 1

    def get_total_price(self):
        total_price = sum([item.price * item.count * self.calculate_discount(item.count) for item in self.products_list])
        return total_price


class CartTest(unittest.TestCase):
    products = [Product('p1', 10, 4),
                Product('p2', 100, 5),
                Product('p3', 200, 6),
                Product('p4', 300, 7),
                Product('p5', 400, 9),
                Product('p6', 500, 10),
                Product('p7', 1000, 20)]
    cart = Cart(products)

    def test_get_total_price(self):
        self.assertEqual(self.cart.get_total_price(), 24785.0)


if __name__ == "__main__":
    unittest.main()
