from random import randint
lista = []
jogos = []
n = int(input('Quantos jogos você quer?'))
c = 1
tot = 1

while tot <= n:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont +=1
            if cont >=6:
                break
    lista.sort()
    jogos.append(lista.copy())
    lista.clear()
    tot += 1
for ind, l in enumerate(jogos):
    print(f'Jogo {ind+1}: {l}')

