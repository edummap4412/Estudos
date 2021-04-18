"""
Conjuntos
- Conjuntos em qualquer linguagem de programação , estamos fazendo referencia a Teoria dos conjuntos da matematica.

- Aqui no Python os conjuntos são Chamdos de Sets.

Dito isso ,  da mesma forma que na matemática:
-Sets (conjuntos) não possuem valores duplicaos:
-Sets (conjuntos) não possuem valores ordenados:

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles.Quando não precisamos se preocupar

Os conjuntos (sets) são referenciados em Pyhton com chaves {}
    - Um dicionario tem chave/valor:
    - Um conjuntotem apenas valor:

"""
# Definindo um conjunto:

#Foram 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})# Repare que temos valores repetidos.

print(s)
print (type(s))
#OBS : Ao crias um conjunto, caso seja adicionado um valor ja existente, o mesmo será ignorado sem gerar error e nao fará parte do conjunto

# Forma 2 - Mais comum

lista = [1, 2, 3, 4, 5, 6, 8, 9, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 56, 7, 7]

print(set(lista))

# importante lembra que além de nao ter valor dulicado nao há ordem dos numeros:

lista = [1, 2, 3, 4, 5, 6, 8, 9, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 56, 7, 7]
print(lista)

dicionario = (lista, 'dict')
print(f'Dicionario:{dicionario}')

