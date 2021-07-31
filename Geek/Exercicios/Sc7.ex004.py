lista = [1, 2, 3, 4, 5, 6, 7, 8]
s=s1=0
for indice, n in enumerate(lista):
    n1 = int(input('Escolha o valor do primeiro vetor :'))
    n2 = int(input('Escolha o valor do segundo vetor:'))
    s = lista.index(n1)
    s1 = lista.index(n2)
    print(f'{s} + {s1} = {s + s1}')

