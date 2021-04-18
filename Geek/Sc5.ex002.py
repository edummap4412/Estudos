
while True:
    n = int(input('Informe o número:'))
    if n > 0:
        r = n**2
        print(f'Raiz quadrada de {n} = {r}')
    if n <= 0:
        print('Número não pode ser negativo....')
        n = int(input('Digite novamente :'))
    op=' '
    while not op in 'SN':
        op=str(input('Quer continuar? [S/N]')).strip().upper()
    if op == 'N':
        break


