
def multiplica(multi):
    mult = multi*4
    return mult


b = [multiplica(a) for a in range(10) if a % 2 == 0]
c = [b for b in range(20)]
d = sum(e for e in range(10))
print(b)
print(c)
print("-----------------------------------")


class Compras:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def total(self):
        return self.preco * self.quantidade

    def descricao(self):
        return self.nome


class Lista:
    def __init__(self, items, promocao=None):
        self.items = list(items)
        self.promocao = promocao

    def valores(self):
        return [item.total() for item in self.items]

    def descreva(self):
        return [descreve.descricao() for descreve in self.items]

    def desconto(self):
        valor = sum(item.total() for item in self.items) * .03
        return sum(item.total() for item in self.items) - valor

    def __len__(self):
        return self.items

    def itensigual(self, v):
        try:
            return self.items.count(v)
        except:
            raise ValueError(f'{v} não existe na lista')
class MaisDesconto(Lista):
    def __init__(self, item, promocao=None, vale=.3):
        Lista.__init__(self, item, promocao)
        self.vale = vale

    def desconto_por_item(self):
        if self.vale:
            if len(self.items) >= 5:
                valor = sum(item.total() for item in self.items) * .8 * self.vale
                return f" Na compra  desconto de 20% o  valor fica : {valor:.2f}"
        else:
            valor = sum(item.total() for item in self.items) * .8
            return valor


class ImpostoQtdade(Compras):
    def __init__(self,nome, preco, quantidade):
        Compras.__init__(self, nome)


carrinho = [Compras('banana', 4, 5),
            Compras('Uva', 5, 9),
            Compras('Pera', 10, 8),
            Compras('Abacate', 20, 4),
            Compras('Abacate', 20, 4),
            ]


def desconto_mais20(lista):
    distinct_items = {item.produto() for item in lista.items}
    return distinct_items


item = Lista(carrinho)
print(item.valores())
print(item.descreva())
print(item.desconto())
print(f"Contem:{len(item.items)} itens")
print(item.itensigual('banana'))

item = MaisDesconto(carrinho)
print(item.desconto_por_item())


"""
lista = []

for n in range(10):
    n = input('Digite Numero:')
    if n not in lista:
        lista.append(n)
    else:
        lista.pop()
        print('elemento já existe na lista . elemento excluido')
        
print(lista)
"""

lista = ['banana','banana','Maça']
print(lista.count('banana'))
