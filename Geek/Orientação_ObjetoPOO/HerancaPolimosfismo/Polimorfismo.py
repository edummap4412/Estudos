"""
POO - Polimorfismo
Poli ->
Morfis ->
"""


class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A Classe filha precisa implementar esse método')

    def comer(self):
        print(f'{self.__nome} está comendo')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)


    def falar(self):
        print(f'{self._Animal__nome} fala wau wau')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala miau')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome}  fala sniff sniff')
canino = Cachorro('Spike')
canino.falar()
canino.comer()
print('-----------')

felino = Gato('Garfield')
felino.falar()
felino.comer()
print('------------')


Ratatullie = Rato('Ferrini')
Ratatullie.comer()
Ratatullie.falar()

print('-----------')

pritn