'''from math import sin,cos,tan,radians
n=int(input('Digite o Angulo :'))
n1=radians(n)
print('seno do angulo é {:.2f}\n tan {:.2f} \n cos {:.2f}'.format(sin(n1),cos(n1),tan(n1)))'''

'''nome=str(input('Digite seu nome :')).strip().split()
nome1= nome.upper()
nome2=nome.lower()
nome3=nome.split()
print('O primeiro A esta em  {}'.format())
print ( 'A ultima letra A esta em  {}'.format(nome3,[len(nome3)]-1))'''
'''s=0
for c in range(1,5):
    n=int(input('Qual sua idade :'))
    s=(s+n)/c

print('Media de idade {:.2f}'.format(s))'''
'''n=0
cont=0
from random import randint
lista=randint(0,10)
while n!= lista :
    n=int(input('Digite um Número :'))
    if n<0 or n>10:
        print('Estou pensando em um número de 0 a 10.Digite novamente:')
        if n!=lista:
            cont+=1
            if n > lista:
             print('Menos...tente denovo')
            if n < lista:
             print('Mais... tente denovo')


print('Você Acertou ,número que pensei foi {},e você precisou de {} tentativas'.format(lista,cont))'''
'''from time import sleep
c1=1
c=1
m=int(input('Digite primeiro Termo :'))
n=int(input('Digite Razão :'))
p=m
while c !=11:
    if c!=11:
        c+=1
        p+=n
        print(p,end=' ')
        if c == 11:
            op=str(input('Você precisa de mais termos?[S/N] ')).upper().strip()[0]

            if op== 'S':
                n2=int(input('Quantos?'))
                m2=11+n2
                if c <= m2:
                    c+=1
                sleep(0.8)
                print('Com mais {} termos Fica {} termos'.format(n2,m2))'''
'''n=int(input('Digite numero'))
n1= n%2
print(n1)'''
'''lista = []
con = 0
while True:
    con += 1
    num = (int(input(f'Digite {con}º: ')))
    lista.append(num)
    for n in lista:
        cont = lista.count(n)
        if cont > 1:
            print('Números reptidos são excluídos')
            lista.remove(n)
    op = ' '
    while not op in 'SN':
        op = str(input('Quer continuar ?[ S/N ]')).strip().upper()
    if op == 'N':
        break
print(sorted(lista))'''

'''lista = []
for c in range(20):
    num = int(input('Digite Número :'))
    lista.append(num)
    for n in lista:
        cont = lista.count(n)
        if cont > 1:
            print('Números repetidos são excluídos')
            lista.remove(n)
print(lista)'''

'''lista = []
for c in range(5):
    lista.append(int(input('Digite Número:')))
    if c == 0 :
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(maior)
print(menor)
for indice , n in  enumerate(lista):
    if n == maior:
        print(f'{indice}')
    if n == menor:
        print(f'{indice}')'''

'''lista = []
while True:
    num = int(input('Digite Número :'))
    lista.append(num)
    for n in lista:
        cont = lista.count(n)
        if cont > 1:
            lista.remove(n)
            print('Numeros Duplicados são excluídos')
    op = ' '
    while not op in 'SN':
        op = str(input('Quer continuar? [S/N]')).strip().upper()
    if op == 'N':
        break
print(lista)'''

'''lista = []
for c in range(10):
    num = int(input('Digite Número :'))
    if num not in lista:
        lista.append(num)
    else:
        print('Número Duplicado.Será Excluído')
print(lista)'''

lista = ['Vasco', 'Palmeira', 'Santos', 'Corinthians']
'''for c in range(0, len(lista)):
    for n in range(0, len(lista)):
        if c != n:
            print(f'{lista[c]} x {lista[n]}')'''



"""lista = []
princ = []

while True:

    lista.append(str(input('Nome: ')))
    lista.append(int(input('Av1: ')))
    lista.append(int(input('Av2: ')))
    princ.append(lista.copy())
    lista.clear()
    op = ' '
    op = str(input('Quer continuar ? [S/N]'))
    if op in 'N':
        break
for ind, p in enumerate(princ):
    print(p[1])
    print(p[2])"""
"""def tabela_de_jogos():
    print('~'*30)
    print(f'{"TABELA DE JOGOS":>22}')
    print('~'*30)

tabela_de_jogos()
lista1 = []
for c in lista:
    for n in lista:
        if c != n:
            lista1.append((f'{c} x {n}'))

for ind, l in enumerate(lista1):
    print(l)"""
s= 0
for c in range(3):
    s += c
    print(s)


lista = list()
lista2 = list()
while True:

    lista.append(str(input('Qual seu nome?')))
    lista.append(int(input('Qual sua idade?')))
    lista2.append(lista.copy())
    lista.clear()
    op=' '
    while not op in 'SN':
        op = str(input('Adionar mais valores?'))
    if op == 'N':
        break
print(lista2)

for ind, c in enumerate(lista2):
    print(c)





