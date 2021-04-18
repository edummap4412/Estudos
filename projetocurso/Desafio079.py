lista = []

while True:
    n = int(input('Digite um número :'))
    lista.append(n)
    cont=lista.count(n)
    if cont > 1:
        print('Números duplicados não podem ser adionados')
        lista.pop()
    else:
        print('Número Adicionado ')
    op = ' '
    op =str(input('Quer continuar? [S/N]'))

    if op == 'N':
        break
print(lista)