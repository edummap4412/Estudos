"""
 -Metodos (funcooes_ > Representam os comportamentos do objeto , Ou seja , as ações que este objeto porde realizar
 no seu sistema

Em Python , dividimos os metodos, em 2 grupos : Metodos  de instancia e Metodos de Classe

Metodos de instância
"""



class Lampada:


    def __init__(self,cor, voltagem, luminosidade):
        self._cor = cor
        self._voltagem = voltagem
        self._luminosidade = luminosidade



class ContaCorrente:

    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__id = ContaCorrente.contador + 1
        self.__numero = numero
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__id

class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

class Usuario:
    def __init__(self, nome, email, senha):
        self._nome = nome
        self._email = email
        self._senha = senha

    def _correr(self,metros):
        print(f'{self.__nome} esta correndo {metros} metros')