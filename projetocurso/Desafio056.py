s=0
nome=' '
maior=0
menor=0
cont=0
maior=0

for c in range(1,3):
    n=str(input('Digite seu nome :'))
    n1=int(input('Digite sua idade :'))
    s=(s+n1)/c
    print('''Seu Sexo é :
    [ 0 ] Homem  ou [ 2 ] Mulher''')

    op= int(input('Escolha :'))
    if op == 0:

        maior=n1
        nome=n

        if maior > n1 :
            maior=n1
            nome=n


    if op == 2:
       menor=n1
       if n1 <= 21:
            cont+=1



print('Maior idade é {} e chama {}'.format(maior,nome))
print('Quantidade de mulheres menores que 20 anos é {}'.format(cont))
print('Media de idade do grupo {:.2f}'.format(s))


