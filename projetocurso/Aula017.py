'''lanche =['hamburguer' ,'pizza','Refri','Sundae']
lanche[3]='Picole'
lanche.append('Sorvete')
lanche.insert(0,'HotDog')
print(lanche)'''
# Listas podem ser alteradas em qualquer momento.
# append adiciona no final da Lista.

#   PARA DELEÇÃO DE ITENS NA LISTA
lista = ['harburguer', 'Batata', 'Refrigerante', 'Sorvete']
lista.remove('Sorvete')
print(lista)
# del.lista[3] = remove item
# lanche.pop('nome do item')

# função list declara listas e podemos tambem usar com range.
valor = list(range(0, 9))
print(valor)

valores = [8, 2, 4, 5, 6, 7, 0]

valores.sort()
valores.reverse()
print(valores)
