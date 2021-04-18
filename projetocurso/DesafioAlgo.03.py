sala = ['B1', 'B2', 'B3', 'B4', 'B5']
sala2 = []

while True:
    cad = str(input('Escolha número da cadeira na Fileira "B":')).strip().upper()
    for ind, cadeira in enumerate(sala):
        if cad == cadeira:
            if cad not in sala2:
                sala2.append(cad)
            else:
                print('Cadeira já escolhida')
    op = ' '
    op = str(input('Quer Escolher mais uma cadeira? [S/N]'))
    if op =='N':
        break
    else:
        if len(sala2) == 5:
            print('Todas as cadeiras foram escolhidas')
            break

print(sala)
print('as cadeiras escolhidas foram:')
for c in sala2:
    print(c,end=' ')

