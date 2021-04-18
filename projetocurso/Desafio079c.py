numeros = []
while True:
    num = int(input('Digite Números:'))
    if num not in numeros:
        numeros.append((num))
    else:
        print('Números repetidos não são adicionados.')
    op =' '
    while not op in 'SN':
        op =str(input('Quer continuar ? [ S/N]')).strip().upper()
    if op == 'N':
        break
print(numeros)


