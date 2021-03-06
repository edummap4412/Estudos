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
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total:{:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):
    """5% de desconto para clientes com mil ou mais pontos no programa de fidelidade"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """10% de desconto para cada LineItem com 20 ou mais unidades"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 1
    return discount


def large_order_promo(order):
    """7% de desconto para pedidos com 10 ou mais itens diferentes"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
