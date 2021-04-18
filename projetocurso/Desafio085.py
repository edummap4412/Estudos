num = [[], []]
for c in range(10):
    numeros = int(input('Digite números:'))
    if numeros % 2 == 0:
        num[0].append(numeros)
    else:
        num[1].append(numeros)
num[0].sort()
num[1].sort()
print(f'Lista de Pares :{num[0]}')
print(f'Lista de Impares:{num[1]}')
