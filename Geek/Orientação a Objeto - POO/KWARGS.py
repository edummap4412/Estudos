"""
    **kwargs
    Poderiamos chamar este parâmettro de **xis, mas por convenção chamamos de **kwargs

    Este é só mais um parâmetro, mas diferente do *args que coloca os valors extras
em uma tupla p **kwargas exige que utilizeos parâmetros nomeados , e transforma esses paraâmetros extras em um dicionário

"""

# Exemplo


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa} é {cor}')


cores_favoritas(marcos='verde',
                julia='amarelo',
                fernanda='azul',
                vanessa='branco')


# OBS: Os parãmetros *args e **kwargs não são obrigatórios.

cores_favoritas()
cores_favoritas(geek='navy')



# Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if "geek" in kwargs and kwargs ['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f" {kwargs['geek']} Geek"


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='especial'))

"""
# Nas nossas funções, podemos ter :
- Parâmetros obrigatórios:
- * args;
- Parâmetros default ( não obrigatórios);
- **kwargs
"""
# Exemplo


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')

    print(kwargs)


minha_funcao(8,'Julia')
minha_funcao(18, 'Ana', 4, 4, 5, 6, 7, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)


# Entenda porque é impornte manter a ordem dos parametros na declaração

# função com a ordem incorreta de parâmetros
def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]

"""
a = 1
b = 2
args =(3,)
instrutor = 'Geek'
kwargs = {'sobrenome' : 'University', 'cargo:Instrutor}

"""

print(mostra_info(1, 2, 3, sobrenome='University', cargo='instrutor'))

# Desempacotar com **kwargs


def mostra_nome(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}
# Não fucinona (errado)
print(mostra_nome(nomes))

# Certo
print(mostra_nome(nome='Felicity'))

# para passar " nomes " precisa fazer:

print(mostra_nome(**nomes))


def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}


soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)


dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)


#OBS! os nomes da chave em um dicionario devem ser o mesmo dos parÂmetros da função

dicionario = dict(d=1, e=2, f=3, nome ='Geek')

soma_multiplos_numeros(**dicionario)

soma_multiplos_numeros(**dicionario, lang='Python')

