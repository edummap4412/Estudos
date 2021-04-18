lista = []
while True :
    n =int(input('Digite um número:'))
    if n not in lista:
        lista.append(n)
        print('Número Adicionado')
    else:
        print('Número Duplicado. Excluído')
    op = ' '
    op = str(input('Quer Continuar ? [S/N]'))
    if op == 'N':
        break
