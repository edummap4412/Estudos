

class Conta():

    def __init__(self, numero, titular, saldo, limite,):
        self.__numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposito(self, valor):
        print(f'Foi depositado {valor}, na conta : {self.__numero}')
        saldo = self.saldo + valor
        return saldo

    def sacar (self, valor):
         print(f'sacou {valor} seu saldo agora é {self.saldo - valor}')
         return valor

    def transfere(self, origem, destino):
        """ metodo transfere2 faz a mesma coisa só que com o codigo melhor escrito e encapsulado"""
        print(f' a conta :{self._Conta__numero} transferiu para conta {self._Conta__numero} valor de R${origem}')
        tras = destino + origem
        return tras

    def transefere2(self,valor, destino):
        self.sacar(valor)
        return destino.deposito(valor)

    def get_saldo(self):
        return self.__saldo
    @property
    def get_titular(self):
        return self.__titular

    #@limite.setter
    def limite(self):
        return self.__limite

    def set_limite(self,limite):
        self.limite = limite

    @staticmethod
    def codigos_bancosI():
        return "Retorna os metodos sem a necessidade de objetos , @staticmethod tem que ser usados com cautela"

conta = Conta(46, "Eduardo", 1155, 10000)
conta2 = Conta(323, "Nico", 255, 12300)
print(conta.get_titular)
# Instancias para metodo antigo (transfere)


# instancias para novos metodos (transfere2)

print(conta2.transefere2(100, conta))

conta.set_limite(100000)
print(conta.limite)

conta.codigos_bancosI()

