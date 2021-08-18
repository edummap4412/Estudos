"""

Conhecendo o Pickle

A função do Pickle é realizar o seguinte processo:

Objeto Python -> Binarização

Binarização -> Objeto Python

Este processo é chamado de Serialização/deserialização

#OBS: O módulo Pickle não é seguro contra dados maliciosos e desta
forma é recomendado trabalhar com arquivos pickle vindos de outras pessoas que você
não conheça ou de fontes desconhecidas.
"""
import pickle


class Animal:

    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.nome} esta comendo...')



class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self._Animal__nome} está miando')


class Cachorro(Animal):
    def __init__(self,nome):
        super().__init__(nome)

    def late(self):
        print(f'{self._Animal__nome} esta latindo...')


"""felix = Gato('Felix')
pluto = Cachorro('Pluto')

# Fazendo a escrita em arquivos pickle

with open('animels.pickle','wb') as arquivo: # wb =  write binary
    pickle.dump((felix, pluto), arquivo)"""


# Fazer a leitura de dados em arquivos Pickle

with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')

    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.late()

