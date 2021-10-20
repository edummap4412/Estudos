class Conta:
    def __init__(self, numero, saldo, limite):
        self.__numero = numero
        self.__saldo = saldo
        self.__tarifaTranferencia = 8.0

    def __valida_transf(self,valor):
         return valor <= self.__saldo
    def transfere(self, valor,destino):

        if self.__valida_transf(valor):
            self.__saldo -= valor

            return destino._Conta__saldo + valor
        else:
            return 'Saldo insuficiente'


conta= Conta(123, 1000,8)
conta2= Conta(123, 1000,8)

print(conta.transfere(100,conta2))
print(conta._Conta__saldo)
conta._Conta__valida_transf

