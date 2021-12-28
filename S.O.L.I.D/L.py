from typing import Type


class PessoaA:
    def se_aprensentar(self):
        print('Ola, sou a Pessoa A')


pessoaA = PessoaA()

pessoaA.se_aprensentar()

class PessoaB:
    def __init__(self):
        super().__init__()

    def se_apresentar(self):
        print('Estou alterando esse metodo')


def aprensentar():
    print('Estou alterando esste metodo')

pessoaA.se_apresentar = aprensentar()

pessoaB = PessoaB()
pessoaB.se_apresentar()

"===================================="

class Animal:
    def comer(self):
        print('O Animal esta Comendo')

    def dormir(self):
        print('O Animal esta Dormindo')

    def andar(self):
        print('O Animal esta andando na Jaula')


class Aves(Animal):

    def __init__(self):
        super().__init__()

    def cantar(self):
        print('A ave esta cantando')

class Pinguim(Aves):
    def __init__(self):
        super().__init__()

    def escorregar(self):
        print('O Pinguim esta escorregando no gelo')


class Pessoa:

    def observar(self, animal: Type[Animal]):
        animal.comer(animal)


eduardo = Pessoa()
animal = Aves
eduardo.observar(animal)


class Conexao:

    def conectar(self):
        print('Conectando ao banco de dados')

    def desconectar(self):
        print('Desconectando ao banco de dados')


class MysqlRepo(Conexao):

    def __init__(self):
        super().__init__()

    def select(self):
        self.conectar()
    print('SELECT * FROM table')


class Postgres(Conexao):

    def __init__(self):
        super().__init__()

    def select(self):
        self.conectar()
        print('SELECT * FROM table')


class CasoDeUso:
     def buscar(self, db_repo: Type[MysqlRepo]):
         db_repo.conectar(db_repo)



usar_banco = CasoDeUso()

banco_selecionado = MysqlRepo

usar_banco.buscar(banco_selecionado)