lista = []
lista2 =[]
lista3= []

'''for ind , n in enumerate(lista):
    if ind % 2 == 0:
        lista3.append(n)
        print(n)
for ind2 , n2 in enumerate(lista2):
    if ind2 % 2 == 1:
        lista3.append(n2)
        print(n2)

print(f'{sorted(lista3)}')'''

for c in range(10):
    num = int(input(f'Digite {c}º Número:'))


    if c % 2 == 0:
        lista3.append(num)
    if c % 2 == 1:
        lista3.append(num)

print(lista3)

