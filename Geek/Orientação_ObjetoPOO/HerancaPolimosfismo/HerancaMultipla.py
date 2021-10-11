"""
POO - Herança Multipla

Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de multiplas classes.
fazendo com que a classe filha herde todos os atributos e métodos de todas
as classes herdadas.

#OBS : A herança múltipla pode ser feita de duas meneiras:
    - Por multiderivação direta:
    - Por Multiderivação Indireta;

# Exemplo 1 - Multiderivação Direta


class Base1:
    pass


class Base2:
    pass


class MultiDerivada(Base1, Base2):
    pass


# Exemplo 2 - Multiderivação Indireta


class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiDerivadas(Base3):
    pass


)BS: Não importa se a derivação é direta ou indireta. Aclasse que realizar a herança ira realizar
os métodos e atributos da superclass
"""

# Exemplo 1 - Multiderivação Direta


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


class Pinguim(Aquatico, Terrestre):
    def __init__(self, nome):
        super().__init__(nome)


# Testando

baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())
print('------------')

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())
print('------------')

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.cumprimentar())

# Objeto é instância de...
print(f'Tux é instancia de Pinguim?{isinstance(tux,Pinguim)}')
print(f'Tux é instancia de Aquatico?{isinstance(tux,Aquatico)}')
print(f'Tux é instancia de Terrestre?{isinstance(tux,Terrestre)}')
print(f'Tux é instancia de object?{isinstance(tux,object)}')
