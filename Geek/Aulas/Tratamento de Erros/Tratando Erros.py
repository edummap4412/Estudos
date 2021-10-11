

"""

Erros mais comuns em python


SyntaxError -> Ocorre quando o pythn encontra um erro de sintaxe. Ou seja, voce escreve
o Python não reconhece como parte da linguaguem:

NameError -> Ocorre quando uma variavel ou funçao nao foi definida

TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

a) print ( len(5))

b) print('Geek' + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista  ou outro
tipo de dado indexado utilizando um indice invalido.


5 - ValueError -> Ocorre quando uma funçaao/operação built-in (integrada)recebe um argumento com tipo correto
mas  valor inapropriado.

print(int('Geek'))

6 -KeyError -> Ocorre quando tentamos acessar um dicionario com uma chave que nao existe


dic = {'python': 'university'}
print(dict['geek'])

7 - AttributeError -> Ocorre quando uma variavel nao tem um atributo/função

tupla = (1,2,31,)
print(tupla.sort())

8 - ItendtationError -> QUando nao respeitamos a indetanção do Python (4 espaços)


"""


class B (Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")

    except C:
        print("C")

    except B:
        print("B")

        
