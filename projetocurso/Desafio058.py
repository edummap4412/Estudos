n=1
cont=1
from random import randint
lista=randint(0,5)
while n !=lista:
    n=int(input('Digite Número que você acha que estou pensando:'))
    if n!= lista:
        cont+=1
        if n<0 or n > 5:
            print('Estou pensando em um número entre 0 a 5')
    if n>lista:
        print('Menos...')
    if n<lista:
        print('Mais...')
    if n == lista:
        print('Parabens você Acertou!!')

print('Adivinhou na {}º tentativa'.format(cont))



