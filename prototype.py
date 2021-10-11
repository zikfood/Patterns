import copy
from abc import ABC, abstractmethod


class Prototype(ABC):
    @abstractmethod
    def clone(self): pass


class Pizza(Prototype):
    """
    Класс компонуемого продукта
    """

    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    def clone(self):
        return type(self)(
            self.size,
            self.toppings,
        )


if __name__ == "__main__":

    pizza = Pizza(23, ('banana', 'onion', 'sausage'))

    print(pizza.toppings, pizza.size)
    new_pizza = pizza.clone()
    new_pizza.toppings = ('pickles', 'apple')
    print(new_pizza.toppings)
    salami_pizza = copy.deepcopy(new_pizza)
    salami_pizza.size = 19
    print(salami_pizza.size)
