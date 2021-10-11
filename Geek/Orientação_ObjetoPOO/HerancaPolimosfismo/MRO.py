"""
POO MRO  - Method Resolution Order

 É ordem de execução dos médotos ( quem será executado primeiro)

 Em python, a gente pode conferir a ordem de execução dos métodos de 3 formas:
    - Via propriedades da classe (ir no Console e chamar Pinguim._mro__)
    - via método MRO()
    - Via  help ir no console e colocar help(Pinguim)

"""


class Animal:
    def __init__(self,nome):
        self.__nome = nome

    def coumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
            return f'{self._Animal__nome} está nadando!'

    def cumprimentar(self):
            return f"Eu sou {self._Animal__nome} do mar"


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)


    def andar(self):
        return f'{self._Animal__nome} está andando'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra'


class Pinguim( Aquatico,Terrestre,):
    def __init__(self, nome):
        super().__init__(nome)


# Testando

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())

"""
Quanto terrestre esta em primeiro
class Pinguim(Terrestre, Aquatico):
    def __init__(self, nome):
        super().__init__(nome)
        
retorna 

Eu sou Tux da terra

Quando Aquatico esta em primeiro
class Pinguim( Aquatico,Terrestre,):
    def __init__(self, nome):
        super().__init__(nome)

retorna 
Eu sou Tux do mar

]"""