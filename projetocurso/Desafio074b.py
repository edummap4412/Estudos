from random import randint
numero = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
for n in numero:
    print(f'{n}',end=' ')

print(f'\nMaior número é :{max(numero)}')
print(f'Menor número é :{min(numero)}')
