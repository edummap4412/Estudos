class Data():
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

class Conta(Data):

    def __init__(self,numero, titular, saldo, limite, dia, mes, ano):
        super().__init__(dia, mes, ano)
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposito(self, valor):
        saldo = self.saldo + valor
        return saldo

    def sacar (self, valor):
         print(f'sacou {valor} seu saldo agora é {self.saldo - valor}')


conta = Conta(123, "Eduardo", 1155, 10000)
conta2 = Conta(123, "Nico", 155, 12300)


print(conta.data(21, 11, 2000))

conta.deposito(500)
conta.sacar(300)
print(conta.saldo)

print(conta2.saldo)

