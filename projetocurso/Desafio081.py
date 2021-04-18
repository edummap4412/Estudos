lista = []
c = 0
while True:
    c += 1
    num = int(input(f'{c}º Número'))
    lista.append(num)
    lista.sort(reverse=True)
    op = ' '
    while not op in 'SN':
        op = str(input(('Quer continuar? [S/N]'))).strip().upper()
    if op == 'N':
        break
print(f' A lista tem {len(lista)} elementos' )
print(lista)
if 5 in lista:
    print('Existe 5 na lista')
else:
    print('Não tem 5 na lista')

