"""
POO - Atributos

Atributo -> Representam as careacteriscas dos objeto . ou seja, pelos atributos nós conseguimos representar compatucionalmente
os estados de um objeto.

Em Phython, Divimos os atributos em 3 grupos:
    - Atributos de instância:
    - Atributos de Classe:
    -Atributos Dinâmicos:

# Atibutos de instância: São atributos declarados dentro do metodo construtor.
# OBS : Metodo construtor :É um método especial utilizado para a contrução do objeto.


"""

class Lampada:


    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False




class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha



# Atributos Públicos ou Atributos Privados
"""
Atributo privado so pode ser declarado dentro da propria classe
em python por convençao , ficou estabelecido que , todo atributo de uma classe é publico . Ou seja , pode ser acessado em todo o projeto.
Caso queiramos demostrar que o determinado atributo deve ser tratado como privado, ou seja, que deve ser acessado/utilizado somente dentro da
propria classe onde é declarado. 
utiliza-se um __ duplo underscore no inicio de seu nome

Isso é conhecido também como Name MangLing

"""

#ATRIBUTOS PRIVADOS
class Acesso:

    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.__email)

# OBS : Lembre-se que isso é apenas uma conveção , ou seja , a linguagem Python não
# vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe.

#Exemplo
user = Acesso('user@gmail.com','12345')

"print(user.__senha) # Da erro de atributo"
print(user._Acesso__senha) # TEmos acesso mais nao deveria fazer esse acesso
user.mostra_senha()
user.mostra_email()



#Atributos de Classe


class Produto:
    #Atributo de classe
    imposto =1.08
    contador = 0

    def __init__(self, nome, valor,):

        self.id = Produto.contador + 1
        self.nome = nome
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('Play4', 3000)
p2 = Produto('Xbox', 2800)

print(p1.nome, p1.valor)
print(p2.nome, p2.valor)
# Acesso ao atributo de classe ( ATRIBUTOS ESTATICOS)

#incorreto
print(p1.imposto) # Mostra porem é incorreto

#correto
print(Produto.imposto) # Correto!


print(p1.id)
print(p2.id)

# com o logica do contador ele ira contar no id o numero de prodtos , o primeiro  self.id recebe 1 e no produto.id =self.id
#ele salva i valor e atualiz adicionando no proximo produto



#Atributos Dinâmicos -> Um atributo de instancia pode ser criado em tempo de execussão
    #OBS : o atributo Dinamico é excluisvo da instancia que criou

p1 = Produto('Play4', 2300)
p1.estoque = 40 # Esse é o atributo dinamico , pertence somente ao p1

print(f'{p1.nome} {p1.valor}, {p1.estoque}')
print(p1.__dict__)

# Para deletar
del p1.estoque
print(p1.__dict__)
