class Orcamento():

    def __init__(self):
        self.__items = []

    @property
    def valor(self):
        total = 0.0
        for item in self.__items:
            total += item.valor
        return total

    def obter_itens(self):
        return tuple(self.__items)

    def adciona_item(self, item):
        self.__items.append(item)

    def total_item(self):
        return len(self.__items)

    @property
    def peso(self):
        total_peso = 0
        for item in self.__items:
            total_peso += item.peso
        return total_peso


class Item():
    def __init__(self, nome, valor,peso):
        self.__nome = nome
        self.__valor = valor
        self.__peso = peso

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome

    @property
    def peso(self):
        return self.__peso
