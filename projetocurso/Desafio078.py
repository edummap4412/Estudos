numeros = []

for c in range(5):
    numeros.append(int(input('Digite um numero:')))
print(numeros)
print(f'O Maior número é {max(numeros)} e sua posição')
for i , n in enumerate(numeros):
    if n == max(numeros):
        print(f'{i} ,',end='')
print()
print(f'O Menor número é {min(numeros)} e sua posição')
for i, n in enumerate(numeros):
    if n == min(numeros):
        print(f'{i},',end='')


