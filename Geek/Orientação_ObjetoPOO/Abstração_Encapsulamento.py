"""
 O grande objetivo da POO  é encapsular o codigo dentro de um grupo logico e hierarquico utilizando classes.

 Encapsular -> cápsula


Abstração , em POO é o ato de expor apneas dados relevantes de uma classe , escondendo atributos e métodos
privados de usuário
"""

class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de  {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >=valor:
                    self.__saldo -= valor
            else:
                print('Saldo Insuficiente')

        else:
            print('O valor deve ser positivo')

    def transferencia (self, valor, conta_destino):

        self.__saldo -= valor

        conta_destino.__saldo += valor



# Testando


conta1 = Conta('Eduardo', 150.00, 1500)
conta2 = Conta('Michael', 300, 10000)




""""# Exemplo ( se nao tiver encapsulado ou seja os atributos estarem publicos)
conta1.numero = 42
conta1.titular = "Xuxa"
conta1.saldo = 99999999
conta1.limite = 99999999999

print(conta1.__dict__)"""

print(conta1._Conta__titular) # Name Mangling

conta1._Conta__titular = "Michael"

print(conta1.__dict__)

conta2.transferencia(100, conta1)

conta1.extrato()
conta2.extrato()

