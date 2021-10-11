from collections import namedtuple

Custumer = namedtuple('Costumer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):

        if not hasattr(self, '__total'):
            if not self.promotion is None:
                discount = self.promotion
                self.__total = sum(item.total() - discount for item in self.cart)
            return self.__total




item = LineItem('Playstation', 1, 5000)
item2 = LineItem('Playstation', 2, 5000)
item3 = LineItem('Playstation', 3, 5000)


order = Order('Fulano',[item, item2, item3], .05)
print(order.total())


