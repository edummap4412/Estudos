

class Conta:
    contador = 400

    def __init__(self, titular, saldo=0, limite=0,):
        self.titular = titular
        self.saldo = saldo
        self.dependentes = []

    def nome(self):
        return f'no do cliente é  {self.titular}'

    def saldor(self):
        while not self.saldo ==2 :
            self.saldo += 1
        return self.saldo



    def deposito(self,grana,*args, **kwargs):
        if not grana:
            return f'Depositos foram feitos mas nao adicionado a conta{kwargs}'
        for k, v in kwargs.items():
            for valor in v:
                grana += valor
            return grana



class Dependentes:
    def __init__(self, nome):
        self.nome = nome


nome = Conta('Eduardo', 2)

print(nome.deposito(4, depositos=[6,6,7,8,9], depositos2= 4))

print(nome.nome())
print(nome.saldo)
print(nome.saldor())
numero = (4,5,6,7)

