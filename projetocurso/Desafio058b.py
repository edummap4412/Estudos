cont=0
from random import randint
computador=randint(0,10)
print('Sou seu computador e pensei em um número entree 0 e 10.')
ad=False
while not  ad:
    n=int(input('Digite um número entre 0 e 10 :'))
    cont+=1
    if n == computador:
        ad=True
        print('Você acertou')
    if n<0 or n>10:
        print('Você digitou um número invalido. estou pensando em um numero de 0 a 10')
    else:
        if n > computador:
            print(' Menos...tente de novo.')
        if n< computador:
            print('Mais... tente de novo.')

print('Numero que pensei foi {}'.format(computador))
print(' Você acertou na {}º tentativa'.format(cont))
