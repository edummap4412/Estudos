'''
LISTA ( list )
Listas em python funcionam como vetores / matrizes (arrays) em outras liguagens,
com a diferença de serem dinamicos e tambem poder colocar QUALQUER tipo de dado.

Linguagens C/Java : Arrays
    - Possuem tamanho e tipo de dado fixo.
    Ou seja se voce criar um Array do tipo int e com tamanho 5 , este array
    sera sempre do tipo inteiro e poredra ter SEMPRE no maximo 5 valores
Já em Python :

-Dinâmico: Não possui tamanho fixo.(pode adcionar a quantidade de elementos que quiser) Enquanto houver memoria
no PC ele pode se adcionado
-Quallquer tipo de dado: As listas  nao possuem tipo de dado.

As listas em Python são representado por ' [] '

'''
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 4, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos Facilmente Checar se determinado valor esta contido na lista
num = 18
if num in lista4:
    print('Encontrei o Número')
else:
    print(f'Não encontrei o Número {num}')

# Podemos facilmente Ordenar uma lista

(lista1.sort())
print(lista1)

(lista2.sort())
print(lista2)

# Podemos contar o numero de ocorrencia de um valor em uma lista
print(lista2.count('e'))

print(lista1.count(1))

# Adicionar elementos em listas
'''
Pàra adicionar valores em lista ultilizamos a função ' append' 
 OBS : com append , nós so conseguimos adicionar 1 valor por vez
'''
print(lista1)
lista1.append(42)
print(lista1)

# Possivel usar um lista dentro do append
lista1.append([8, 3, 1])  # Coloca lista como valor unico (Sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não Encontrei')

lista1.extend([3, 4, 1])  # Coloca cada valor da lista como valor adicional á lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do indice
# OBS : Isso não substitui o valor inicial o mesmo será deslocado para a direita da

lista1.insert(2, 'Novo valor')
print(lista1)

# Podemos JUNTAR duas listas
'''lista1 = lista1 + lista2
print(lista1)'''

# Podemos fazer de Trás pra frente
lista1.reverse()
lista2.reverse()

print(lista1)
print(lista2)
# OBS : Usar o Slice tambem funciona  [::-1]

# Podemos copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Podemos remover o ultimo valor da lista
lista5.pop()
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo indice
# OBS : Os valores  a direita deste indice são deslocados para esquerda
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos
lista5
print(lista5.clear)
print(lista5)

# Podemos repetir elementos numa lista
nova = [1, 2, 3, 4, ]
nova1 = nova * 3
print(nova1)

# converter String para  uma Lista

curso = 'Programação Python'
cruso1 = curso.split()
print(cruso1)

# Exemplo 2
curso = 'Programção,em,Python,Essencial'
curso1 = curso.split(',')  # << separador aqui é um virgula ','
print(curso1)

# Converter uma Lista para String
lista6 = ['Programação', 'em', 'Python']
lista6 = ' '.join(lista6)  # << separador pode ser separado tanto com 'espaços ( ' ') como para qualuer outro caracter
print(lista6)

# Iterando sobre LISTA

# Exemplo 1
lista10 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
soma = 0
for n in lista10:
    soma = soma + n
print(soma)

# Exemplo 2
carrinho = []
produto = ' '
while not produto in 'Sair':
     produto = str(input('Adicione mais produtos ou digite "Sair" para Sair' ))
     if produto != 'Sair':
         carrinho.append(produto)
for produto in carrinho:
    print(produto)

#Fazemos acesso aos elementos de forma indexada

cores = ['verde', 'Amarelo', 'Azul', 'Branco']
print(cores[0])
print(cores[-1])


'''for c in cores:
    print(cores)
indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1'''

for indice, n in enumerate(cores):
    print(indice[cores][0])


'  METODOS NÃO TÃO IMPORTANTES MAS UTEIS '
numeros =[1, 2, 4, 5, 4, 6, 5]
# Encontrar o indice de um elemento na lista
print(numeros.index(5,1))# para encontrar apartir do indice 1

# Podemos fazer busca dentro de um range ,inicio /fim
print(numeros.index(5,3,6))

# Revisando Slice (FATIAMENTO)
#lista[inicio:fim:passo]
#Traabalhando  com slice de lista com o parametro 'Inicio"
lista =[1, 2, 3, 4, 5]
print(lista[::1])

# invertendo
nome = [' Eduardo', 'Michael']
nome.reverse()
print(nome)

#Soma , Valor maximo , Valor minimo , tamanho
# * Se os valores forem todos inteiros ou reais

lista9 = [1, 2, 3, 4, 5, 6]
print(sum(lista9))# soma a lista
print(max(lista9))# maximo
print(min(lista9))#minimo
print(len(lista9))#tamanho da lista

#transformando em Tupla

tupla = tuple(lista9)
print(tupla)

# Desempacotamento de lista

lista11 = [1, 2, 3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)

# Copiando uma lista para outra (Shalllow Copy e Deep Copy)

#Forma 1 - Deep Copy
lista12 = [1, 2, 3]
print(lista12)

nova = lista12.copy()

print(nova)

nova.append(4)

print(lista12)
print(nova)
# Usar o Copy as listas ficam independentes ou seja se altera uma a outra nao altera. isso se chama Deep Copy

#Forma 2 - Shallow Copy

lista12 = [1, 2, 3]
print(lista12)

nova = lista # copia
print(nova)

nova.append(4)

print(lista)
print(nova)

# Fazendo a atribui nova = lista criamos um Shallow copy , pois ele altera duas listas de forma igual

