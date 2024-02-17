"""
You have to create a main course and a dessert at an Italian and a French restaurant, but you won't mix one cuisine with the other. 

Your task is:

1) define a class Product with an abstract method cook(). This class would be base class for the next classes:

- class FettuccineAlfredo with field name ("Fettuccine Alfredo"), method cook() provides an output 
of the formatted string "Italian main course prepared: " and name of the dish;

 - class Tiramisu, with field name ("Tiramisu"), method cook() provides an output of the formatted
string "Italian dessert prepared:" and name of the dish;

- class DuckALOrange, with field name ("Duck À L'Orange"), method cook() provides an output 
of the formatted string "French main course prepared: " and name of the dish;

- class CremeBrulee,  with field name ("Crème brûlée"), method cook() provides an output
 of the formatted string "French dessert prepared: " and name of the dish.

2) define a class Factory with an abstract method get_dish() that takes  type_of_meal as a parameter. 
This class would be base class for the classes ItalianDishesFactory and FrenchDishesFactory. The method get_dish() according to type_of_meal ("main" or "dessert") invokes the dish of appropriate cousine;

3) define a class FactoryProducer with the method get_factory(). 
The method takes the parameter type_of_factory and invokes the appropriate dishes factory 
(classes ItalianDishesFactory or FrenchDishesFactory).
"""

import abc
from abc import ABC


class FactoryProducer:

    def get_factory(self, type_of_factory):
        if type_of_factory == 'italian':
            return ItalianDishesFactory()
        return FrenchDishesFactory()


class Factory:

    @abc.abstractmethod
    def get_dish(self, type_of_meal):
        pass


class ItalianDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        if type_of_meal == 'main':
            return FettuccineAlfredo
        return Tiramisu


class FrenchDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        if type_of_meal == 'main':
            return DuckALOrange
        return CremeBrulee


class Product(ABC):

    @abc.abstractmethod
    def cook(self):
        pass


class FettuccineAlfredo(Product):

    @staticmethod
    def cook():
        dish = "Fettuccine Alfredo"
        print(f"Italian main course prepared: {dish}")


class Tiramisu(Product):

    @staticmethod
    def cook():
        dish = "Tiramisu"
        print(f"Italian dessert prepared: {dish}")


class DuckALOrange(Product):

    @staticmethod
    def cook():
        dish = "Duck À L'Orange"
        print(f"French main course prepared: {dish}")


class CremeBrulee(Product):

    @staticmethod
    def cook():
        dish = "Crème brûlée"
        print(f"French dessert prepared: {dish}")



fp = FactoryProducer()
fac = fp.get_factory("italian")
main_dish = fac.get_dish("main")
main_dish.cook()