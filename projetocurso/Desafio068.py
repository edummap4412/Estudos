from random import randint
cont=0
n=0
escolha= ' '
while True:
    n=int(input('Digite o valor'))
    escolha=str(input('PAR OU IMPAR ?')).strip().upper()
    lista=randint(0,10)
    soma=lista+n
    print(soma)
    if soma % 2==0:
        print('É Par')
        if escolha =='PAR':
            print('Jogador vence')
            cont+=1
        else:
         print('Maquina vence')
         break
    if soma %2 ==1:
        print('É impar')
        if escolha == 'IMPAR':
            print('Jogador vence')
            cont+=1
        else:
         print('Maquina vence')
         break
print(f'Jogador ganhou {cont} vezes antes de ser derrotado')
