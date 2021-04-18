from time import sleep
cardapio=True
p = 0
cont = 0
mesas2 = 10
mesas4 = 8
mais=0
op=' '
while cardapio != False :
    while p != 'N':
        n = int(input('Quantas pessoas chegaram Fila:'))

        p = str(input('Deseja adcionar mais pessoas a lista ? [S/N]')).upper().strip()
        if n == 4:
            cont += 1
            print('Quantidade de mesas restantes para 4 pessoas é {}'.format(mesas4 - cont))

            sleep(0.8)
            op=str(input('Há pessoas com deficiencia?'))
            op=True
            if op == 'S':
                sleep(0.8)
                print ('Retirar cadeira')
        if n == 2 :
            cont+=1
            print('Quantidad de mesas Restantes para 2 pessoas é {}'.format(mesas2-cont))
        else:
            print('Instruir cliente a mesas especias')

    print( '''CARDAPIO
     [ 1 ] Filé de Frango
     [ 2 ] Carne ao Molho
     [ 3 ] Feijoada
     [ 4 ] Maminha com arroz
     [ 5 ] pedido finalizado''')

    cardapio=int(input('Escolha opção:'))
    if cardapio == 1:
        cont+=1
        print('Valor de 10,90 x {} = {}'.format(cont,10.90*cont))

    if cardapio == 5 :
        cardapio=False
