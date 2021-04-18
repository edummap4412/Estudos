'''
Tuplas
1 - Usam parenteses
2 - São Imutaveis

'''
tupla1 =(1, 2, 3, 4, 5, 6)

# CUIDADO 2 : Tuplas com 1 elemento:
# somente um argumento dentro dos (4) não é uma tupla.
# SE DENTRO DO PARENTESES (4,) HOUVER VIRULA É CONSIDERADO UMA TUPLA.
# Tuplas são definidas com parenteses

# Gerar TUPLA com range
tupla = tuple(range(11))
print(tupla)

#Desempacotamento de TUPLA
tupla = ('Geek University', 'Programação em Python ')
escola,curso = tupla
print(escola)
print(curso)

''' Concatenação de tupla
 Concatenação de tupla é soma das tuplas'''

tupla2 = (1, 2, 4)
print(2 in tupla2)

#Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('b'))

# Dicas pra usar Tuplas

# Devemos usar tuplas sempre que nao precisamos mudar os dados contidos numa coleção

# Exemplo 1
meses = ( 0,'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio',
          'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
          'Novembro', 'Dezembro')
for indice, numero in enumerate(meses):
    numero = int(input('Digite Número:'))
    print(meses[numero])


