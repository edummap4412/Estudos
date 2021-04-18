op=0
n=int(input('Digite um Número :'))
n1=int(input('Digite outro Número :'))
while op!= 5 :

    if op== 4 :
        print('Digite novamente:')
        n=int(input('Digite um Número :'))
        n1=int(input('Digite outro Número :'))
    print('''
    [ 1 ] Somar
    [ 2 ]multiplicar
    [ 3 ]maior
    [ 4 ] novos números
    [ 5 ]Sair do programa''')

    op=int(input('Escolha Opção :'))
    if op == 1:
        print( 'Soma entre {} e {} é {}'.format(n,n1,n+n1))
    if op == 2:
        print('Multiplicação entre {} e {} é {}'.format(n,n1,n*n1))
    if op == 3:
        if n > n1:
            print('{} maior que {}'.format(n,n1))
        elif n == n1:
            print('Os números são iguais')
        else:
            print('{} maior que {}'.format(n1,n))
    if op == 5 :
        print('BONS ESTUDOS!!')
    if op >= 6:
        print('Opção Invalida')








