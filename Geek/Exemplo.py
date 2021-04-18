'''lista = ['Edu', 'Maria', 'Joaquim']
while True:
    for indice , n in enumerate(lista):
        print(f'Nome do convidado é {n} e seu lugar é {indice}')
    op = ' '
    nome = ' '
    while not op in 'SN':
        op = str(input('Havera mais convidado  ? [S/N]'))
        if op == 'S':
            lista.extend(str(input('Adicione os nomes :'))'''

# AMANHA COTINUAR CRIANDO LISTA DE CONVIDADOS
'''lista1=[1, 2, 3, 4, 5, 6, 7, 8, 9, ]
s = 0
for elemento in lista1:
    s+=elemento
print(s)'''
'''lista = list(range(11))
print(lista)
lista.reverse()
print(lista)
ret= lista.pop()
print(lista)
print(ret)
print(lista.index(4))
print(lista[3:7:1])

#novo = lista.copy()#<- Deep copy
novo = lista#<- Shallow copy
novo.insert(8, 8)

print(novo)
print(lista)
lista2 = [2, 4, 5, 1, 9, 10, 3, 6]
lista2.extend([4, 4, 5])
lista2.sort()
lista2.append([3, 4, 5])
print(lista2)'''

# DICIONÁRIO

'''paises = {'br': 'Brasil','eua':'Estados Unidos','ru': 'Rússia'}
print(paises)
print(paises.get('br'))
print(paises.get('jp', 'Desconhecido'))
print('br'in paises)
novo = {'jp':'Japão'}
paises.update(novo)
print(paises'''

'''paises = {}.fromkeys(['nome', 'usuario', 'email'],'Desconhecido')
print(paises)

paises1 = {}.fromkeys(range(1, 11), 'novo')
print(paises1)'''

'''vetor = [ 1, 3, 5, 6, 7, 7]
vetor0 = vetor[0]
vetor1 = vetor[1]
vetor2 = vetor[3]'''

'''vetor = [1, 0, 3, 5, 7, 8]
vetor0 = vetor[0]
vetor2 = vetor[2]
vetor3 = vetor[5]
soma = sum(vetor.index()) + sum(vetor.index(1)) + sum(vetor.index(5))
print(soma)'''

'''n=int(input('Número:'))
n1=int(input('Outro Número:'))
s = n + n1
if s % 2 == 0:
    print('Par')
else:
    print('impar')'''

'''n = int(input('Digite Número: '))
n1 = int(input('Outro Número: '))
if n < n1:
    for c in range(n, n1):

        print(c, end=' ')
else:
    for c in range(n,n1,-1):
        print(c)'''
f = 1
while True:
    n = int(input('Digite um Número: '))
    for c in range(n, 0, -1):
        f *= c
        print(f'{c} x', end='')
        print(f' = {f}')
    op = str(input('Quer continuar?[S/N]')).strip().upper()
    if op in 'N':
        break
