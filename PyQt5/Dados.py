import random
from random import randint
a=['Sim','Não']
dados= list()
lista = list()

for c in range(500):
    lista.append(random.choice(a))
    lista.append(randint(00000000000, 99999999999))
    lista.append(randint(1500, 7000))
    dados.append(lista.copy())
    lista.clear()
for ind, c in enumerate(dados):
    print(f'{c}')

