"""
 -Metodos (funcooes_ > Representam os comportamentos do objeto , Ou seja , as ações que este objeto porde realizar
 no seu sistema

Em Python , dividimos os metodos, em 2 grupos : Metodos  de instancia e Metodos de Classe

Metodos de instância
"""


class Lampada:

    def __init__(self,cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade


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

    def desconto(self,porcentagem):
        """Retorna o valor do produto com o desconto"""

        return(self.__valor * (100 - porcentagem)) / 100


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0
    @classmethod
    def conta_usuarios(cls): # convensão utilizada para  ser uma classe
        print(f'Temos {cls.contador} usuários no sistema')

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__id = Usuario.contador + 1
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds= 200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuario criado :{self.__gera_usuario()}')


    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome} '

    def checa_senha(self):
        if cryp.verify(senha, self.senha):
            return True
        return False

    def correr(self, metros):

        print(f'{self.nome} esta correndo {metros} metros')

    def __gera_usuario(self):
        return self.__email.split('@')[0]


p1 = Produto('Playstation 4 ', 'Video Game ', 2300)
print(p1.desconto(30))







'''nome = input('Nome')
sobrenome = input('Sobrenome')
email = input('Email')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha:')


if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('SENHAS NAO CONFERE')

senha = input('Informe senha para acesso')

if user.checa_senha:
    print('Acesso permirtido')

else:
    print('Acesso negado')


print(f'Senha User Criptografada : {user._Usuario__senha}')
'''


# Métodos de Classe

class Usuario2 :

    contador = 0
    exemplo = 'Tenho dúvidas de como usar essa cls de outra forma'

    @classmethod
    def exemplos(cls):
        print(f'{cls.exemplos}')

    @staticmethod
    def lembrete():
        return f'Hoje está frio muito frio'

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.id = Usuario2.contador + 1
        Usuario2.contador = self.id


user2 = Usuario2('Eduardo', 28)
user3 = Usuario2('Juca', 29)
user4 = Usuario2('Maria', 28)

user2.exemplos()
print(user2.lembrete())



print(f'{user2.nome}, {user2.idade}, {user2.id}')
print(f'{user3.nome}, {user3.idade}, {user3.id}')
print(f'{user4.nome}, {user4.idade}, {user4.id}')


# Métodos de Classe

user = Usuario('Eduardo', 'Mascarenhas','eduardomascaraehas@gmila.com', '12345')

user.conta_usuarios()


# Método privado

user = Usuario('Eduardo', 'Mascarenhas','eduardomascaraehas@gmila.com', '12345')


print(user._Usuario__gera_usuario())


# Método Estático

print(Usuario.contador)
print(Usuario.definicao())

user = Usuario('Eduardo', 'Pereira','eduardopereira@gmila.com', '12345')

print(user.contador)
print(user.definicao())

