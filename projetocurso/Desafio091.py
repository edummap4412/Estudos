from random import randint
from time import sleep
dados = dict()
for c in range(4):
    dados['jogador'] = randint(1, 6)
    sleep(1)
    for v in dados.values():
        print(f'O Jogador {c+1} tirou {v}')

print(dados)