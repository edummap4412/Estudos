lista = list(range(4))
lista2 = lista.copy()

for ind, n in enumerate(lista):
    for ind2, n1 in enumerate(lista2):
        n2 = int(input(f'Digite numero nas posiçõe [{ind}] e [{ind2}]: '))
        lista.append(n2)

print(lista)
