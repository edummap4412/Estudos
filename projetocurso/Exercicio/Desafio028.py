from random import randint
from time import sleep
pc=int(input('Advinhe o numero que estou pensando de 0 a 5 :'))
lista=randint(0,3)
print('A resposta está E...')
sleep(2)
if pc == lista:
    print('EXATA!!')
else:
    print('ERRADA...')
print(' O numero que pensei foi {}'.format(lista))







