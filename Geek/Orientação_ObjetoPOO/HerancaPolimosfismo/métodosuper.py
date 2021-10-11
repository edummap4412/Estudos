"""
POO - método super()

O método super() se refere á super classe



"""


class Animal():
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'{self.__nome} faz {som}')


class Gato(Animal):

    def __init__(self, nome, especie, raca):
        super.__init__(nome, especie)
        super().faz_som("miau")
        self.__raca = raca

mortadela = Gato('Mortadela', 'Felino',  'Tricolor')
mortadela.faz_som("Miau")

gato = Gato('guri', 'felino', 'tricolor')
