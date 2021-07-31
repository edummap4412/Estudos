"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer. Isso significa que você poderá chamar de qualquer coisa,
desde que comece com asteriscos

Exemplo

*xis

Mas por convenção, Utilizamos * args para defini-lo

mas oque é o *args?



O parâmetro *args utilizado em uma função , coloca os valores extras informados como entrada em uma tupla. Então desde já
lembre-se que tuplas são imutáveis.


# Exemplos

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

# Entendendo o args


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros(1))
print(soma_todos_numeros(1, 2, ))
print(soma_todos_numeros(5, 6, 7, 8, ))


# outro exemplo

def soma_todos_numeros(nome, email, *args):
    return sum(args)


print(soma_todos_numeros('Angelina', 'Jolie',))
print(soma_todos_numeros('Angelina', 'Jolie', 1, 2, ))
print(soma_todos_numeros('Angelina', 'Jolie', 5, 6, 7, 8, ))


print(soma_todos_numeros(5, 6, 7))
"""



# Outro Exemplo de utilização do *args

def verifica_info(*args):

    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek'
    return ' NãoFunciona'


print(verifica_info())
print(verifica_info('University', 'Geek'))
print(verifica_info(1,'University', 3.145))


def soma_todos_numeros(*args):
    return sum(args)



numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9,]


print(soma_todos_numeros(1))
print(soma_todos_numeros(1, 2, ))
print(soma_todos_numeros(5, 6, 7, 8, ))

#Desempacotador

print(soma_todos_numeros(*numeros))



# OBS: O asterisco serve para que  informemmos ao python que estamos
#passando como argumento uma coleçao de dados. Desta froma, ele saberá
#que precisará antes desempacotar estes dados.
