sexo=''
c=1
cont=cont3=cont2=cont1=0
op=''
idade=int(input('Idade :'))
while op != 'N':
    while sexo != 'M' and sexo != 'F':
        sexo=str(input('Qual seu sexo ? [M/F]')).strip().upper()
        if sexo == 'F':
            cont+=1
            if idade <= 20:
                cont1+=1
        if sexo == 'M':
            cont2=1
    op=str(input('Quer continuar ? [S/N]')).strip().upper()

    if op == 'S':
        idade=int(input('Digite sua idade:'))
        cont3+=1
        sexo=str(input('Qual seu sexo ? [M/F]')).strip().upper()
        if sexo =='F':
            cont+=1
            if idade <=20:
                cont1+=1
        if sexo == 'M':
            cont2+=1
        print(f'>>>>>>>{cont3+1}º PESSOA CADASTRADA<<<<<<<<')
print(f'Quantidade de mulheres são {cont} e com menos de 20 anos são {cont1}')
print(f'Quantidade de Homens é igual {cont2}')
print(f'Total de pessoas registradas {cont3+1}')







#CONTINUAR AMANHA ! COMEÇAR REVISANDO E REFAZENDO O DESAFIO 065
