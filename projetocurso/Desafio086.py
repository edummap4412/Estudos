matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma =scol = slin= mai = soma1 = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if matriz [1][c] > mai:
            mai = matriz[1][c]
for l in range (0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]',end=' ')
    print()

print(mai)
for c in range(0, 3):
    slin += matriz[2][c]
print(slin)

for l in range(0, 3):
    scol += matriz[l][2]
print(scol)
