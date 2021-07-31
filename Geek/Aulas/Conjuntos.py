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
#Dicionarios nao aceitao chaves dupliadas
dicionario ={}.fromkeys(lista, 'dict')
print(f'Dicionario:{dicionario}')

#Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1,'b',True,34.22,44}
print(s)
print(type(s))

#Podemos iterar em um set normalmente
for valor in s:
    print(valor)

#Usos interessantes com sets

"Imagine que fizemos um formulario de cadastro de visitantes em uma feira ou museu"
"E os visitando informam manulamente a cidade de onde vieram"

# Nós adicionamos cada cidade em uma lista Python , já que em uma lista podemos adicionar e ter repetição

cidades = ['Belo Horizonte','São Paulo','Campo Grande','Campo Grande','São Paulo','Cuiaba']
print(cidades)
print(len(cidades))
print(set(cidades))


# Adicionando elementos em um  conjunto
s ={1,3}
s.add(4) # nao aceita duplicidades , entao nao da erro mas tambem nao adiciona
print(s)

#para remover
s.remove(3)
# Ou
s.discard(3)
#Remover todo o conjuto
s.clear()

# Copiando um conjunto para outro...
s = {1, 2, 3}
print(s)

# Forma 1 - Deep Copy

novo =s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

#Forma 2 -ShallowCopy
novo = s

novo.add(4)
print(novo)
print(s)

# Métodos Matematicos de Conjuntos

# Imagine que temos dois conjuntos : Um contendo estudantes do curso Python e um
# contendo estudantes do curso de Java.

estudante_python = {'Marcos','Patricia','Ellen','Pedrdo','Julia','Guilherme'}
estudante_java ={'Fernando','Gustavo','Julia','Ana','Guilherme'}

# Veja que alguns alunos que estudam Python também estudam Java

# Forma 1 - Uyilizando Union

unicos = estudante_java.union(estudante_python)
#{'Guilherme', 'Fernando', 'Ellen', 'Julia', 'Ana', 'Marcos', 'Pedrdo', 'Gustavo', 'Patricia'}
print(unicos)

#Forma 2 - Utilizando o caractere pipe " | "
unicos2 = estudante_java | estudante_python
print(unicos2)

"Gerar um conjunto de estudantes que estao em ambos os cursos"

ambos1 = estudante_python.intersection(estudante_java)
print(ambos1)

#Forma2 Utilizando o &

ambos2 = estudante_java & estudante_python
print(ambos2)

# Gerar um conjunto de estudantes que nao esao no outro curso

so_python = estudante_python.difference(estudante_java)
print(so_python)

so_java = estudante_java.difference(estudante_python)
print(so_java)

#Soma,Valor Maximo, Valor Minimo, Tamanho

# Se os valores forem todos inreiros ou reais

s={1, 2, 3, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))

