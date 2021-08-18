from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Cliente','pontos fidelidade')


class LineItem:
    def __init__(self, produto, quantidade, preco):
        self.produto = produto
        self.quantidade = quantidade
        self.preco = preco

    def total(self):
        return self.preco * self.quantidade


class Order:# o Contexto
    def __init__(self, cliente, carrinho, promocao=None):
        self.cliente = cliente
        self.carrinho = list(carrinho)
        self.promocao = promocao

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.carrinho)
        return self.__total

    def vencimento(self):
        if self.promocao is None:
            desconto = 0
        else:
            desconto = self.promocao.desconto(self)

        return self.total() - desconto

    def __repr__(self):
        fmt = '<Order Total: {:.2f} desconto: {:.2f}>'
        return fmt.format(self.total(), self.vencimento())


class Promocao(ABC):# Estratégia : uma classe-base abstrata
    @abstractmethod
    def desconto(self, order):
        """Devolve o desconto como um valor positivo em dólares"""


class FidelityPromo(Promocao):# primeira Estrátégia Concreta
    """ 5% de desconto para clientes com mil ou mais pontos no programa de fidelidade"""

    def desconto(self, order):
        return order.total() * .05 if order.cliente.fidelidade >= 1000 else 0


class BulkItemPromo(Promocao): # Segunda Estratégia Concreta
    """10% de desconto para cada LineItem com 20 ou mais unidades"""

    def desconto(self, order):
        desconto = 0
        for item in order.carrinho:
            if item.quantidade >= 20:
                desconto += item.total() * .1
        return desconto


class LargeOrderPromo(Promocao):#terceira Estratégia Concreta
    """7% do desconto para pedidos com 10 ou mais itens diferentes"""

    def desconto(self, order):
        items_distintos = {item.produto for item in order.carrinho}
        if len(items_distintos) >= 10:
            return order.total() * 0.7

        return 0


Joe = Customer('John Doe', 0)
Ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5),
        LineItem('maçã', 4, 1.5),
        LineItem('melancia', 5, 5.5)]

order = Order(Joe, cart, FidelityPromo())
print(order)
order = Order(Ann, cart, FidelityPromo())
print(order)
print(order.total())
