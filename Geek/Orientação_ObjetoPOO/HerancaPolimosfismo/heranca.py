"""
POO - HerancaPolimosfismo (Inheritance)

A ideia de Herança é a de reaproveitar código.
Também extender nossas classes

OBS: Com a herança, a aprtir de uma classe existente , nós extendemos outra classe
que passa a herdar atributos e métodos da classe herdada.

Cliente
    - nome:
    -sobrenome:
    - cpf:
    - renda:

Funcionario
    - nome:
    - sobrenome:
    - cpf:
    - matricula:

Perguntar :  Existe alguma entidade genérica o suficiente para encapsular os atributos
e métodos comuns a outras entidades?

class Cliente:
    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
         return f"{self.__nome} {self.__sobrenome}"


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


cliente = Cliente('Angelina', 'Jolie','1234.123.1234', 5000)
cliente2 = Funcionario('Felicity','Jones','987.345.345-23',1234)

print(cliente.nome_completo())
print(cliente2.nome_completo())

# REFATORADA COM HERANCA
class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):

    def __init__(self,nome, sobrenome, cpf ,matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula



cliente = Cliente('Angelina', 'Jolie','1234.123.1234', 5000)
cliente2 = Funcionario('Felicity','Jones','987.345.345-23',1234)

print(cliente.nome_completo())
print(cliente2.nome_completo())

print(cliente.__dict__)
print(cliente.__sizeof__())

"""

# Sobrescrita de Métodos(Overriding)
 # Sobrescrita de método, ocorre quando reescrevemos/reimplementam um método presente na super classe
 #em classes filhas

class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):

    def __init__(self,nome, sobrenome, cpf ,matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f"Funcionário:{self.__matricula}, Nome:{self._Pessoa__nome} , Nome completo :{super().nome_completo()}, CPF:{self._Pessoa__cpf}"


cliente = Cliente('Angelina', 'Jolie','1234.123.1234', 5000)
cliente2 = Funcionario('Felicity','Jones','987.345.345-23',1234)

print(cliente.nome_completo())
print(cliente2.nome_completo())

print(cliente.__dict__)
print(cliente.__sizeof__())




