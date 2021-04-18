lista = []
for c in range(5):
    lista.append(int(input('Digite Número :')))
    if c == 0:
        maior = 0
        menor = 0
    else:
        if lista[c] > maior:
            maior = lista[c]

        if menor > lista[c]:
            menor = lista[c]
print(f'Os numeros digitados foram {lista} o maior é {maior} o menor é {menor}')
for indice ,n in enumerate(lista):
    if n == maior:
        print(f'{indice}...')
