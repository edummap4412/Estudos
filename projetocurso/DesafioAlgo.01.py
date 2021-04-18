lista = ['Vasco', 'Botafogo', 'Corinthians']
lista2 =lista.copy()

for c in range(1):
    for ind, n in enumerate(lista):
        for ind1, n1 in enumerate(lista):
            if n != n1:
                print(f'{n} x {n1}')

print('Bom Jogo')
