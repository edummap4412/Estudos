"""
POO - Objetos

Objetos são instancias da classe , ou seja, após o mapeamento do objeto do mundo real
para sua representação computacional, devemos poder criar quantos objetos foram necessarios. Podemos pensar nos objetos/
instâncias de uma class como variaveis do tipo definido na classe.
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__lminosidade = luminosidade
        self.__ligada = False


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf



class Conta:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente2 = self.__numero

    def mostra(self):
        print(f'Dados da clientes:{self.__cliente._Cliente__nome}')

lamp1 = Lampada('branca',110,60)

cli1= Cliente('eduardo', '1231.1331.312')

cc1= Conta(5000, 20000, cli1)