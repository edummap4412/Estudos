"""
POO - Propriedades = Properties


Em liguagens de programação como o Java, ao declararmos atributos privados nas classes, costumamamos a crias
métodos públicos para manipulação desses atributos. Esses metodos são conhecidos por getters e setters, onde os getters retornam
o valor do atributo e os setters alteram o valor do mesmo.

class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador +=1

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depoistar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


conta = Conta('Felicity', 3000, 5000)
conta1 = Conta('Angelina', 2000, 4000)


#Para somar os dois saldos dos clientes com get


soma = conta.get_saldo() +  conta1.get_saldo()
print(f'Asoma do saldo das contas é {soma}')

print(conta.extrato())
print(conta1.extrato())


#Atençao ao uso de set. pois ele altera o valor
print(conta1.__dict__)
conta1.set_limite(999999)
print(conta1.__dict__)

"""



class Conta:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador +=1

    @property
    def numero(self):
        return self.__numero

    @property
    def limite(self):
        return self.__limite

    @property
    def saldo(self):
        return self.__saldo

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @saldo.setter
    def saldo(self, novo_saldo):
        self.__saldo = novo_saldo

    def extrato(self):
        return f'Saldo de {self.__saldo} do cliente {self.__titular}'

    def depoistar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @property
    def valor_total(self):
        return self.__saldo + self.__limite

conta = Conta('Felicity', 3000, 5000)
conta1 = Conta('Angelina', 2000, 4000)


"""Para somar os dois saldos dos clientes com @propety """

soma= conta1.saldo + conta.saldo
print(f'Soma do saldo das contas é {soma}')


"""Para retornar alterar valores usar @nomedometodo.setter"""
print(conta.__dict__)
conta.limite = 999998
print(conta.__dict__)
print(conta.limite)
"Metodo como propriedade tambem é possivel"
print(conta.valor_total)
print(conta1.valor_total)
