print('VOTE NO MELHOR JOGADOR')
lista = []
lista2 = []
cont = 0
while True:

    n = int(input('insira o numero da camisa 1 a 23:'))
    if n != 0:
        lista.append(n)
        lista.count(n)
        if n not in lista2:
            lista2.append(n)
    else:
        break
print('RESULTADOS DOS VOTOS')

print(f'Foram computados {len(lista)} votos')

for ind, l in enumerate(lista2):
    print(f' O jogador camisa : {l}, recebeu: {lista.count(l)} votos')

print(lista2)