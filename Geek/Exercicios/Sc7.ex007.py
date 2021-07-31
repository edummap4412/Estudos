vetor = []
for c in range(1, 5):
    vetor.append(int(input(f'Digite {c}º numero')))
for indice, n in enumerate(vetor):
    n1 = max(vetor)
print(f'Maior número é {max(vetor)}.Na posição {vetor.index(n1)}')

