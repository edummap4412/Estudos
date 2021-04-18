while not 'M' or 'F':
    sexo=str(input('Qual seu Sexo ?')).strip().upper()[0]
    if sexo == 'M' or sexo =='F':
        op=str(input('Opção correta ? [S/N]')).strip().upper()
        if op== 'S':
            print('Sexo Confirmado')
        else:
            print('Opção digite novamente:')
    else:
        print('Opão Invalida')




