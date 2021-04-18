'''import uteis


num = int(input('Digite um valor:'))
fat = uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro  de {num} é {uteis.dobro(num)}')
print(f'O triplo de {num} é {uteis.triplo(num)}')'''

from Uteis import Números

num = int(input('Digite um valor: '))
fat = Números.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {Números.dobro(num)}')
print(f'O triplo de {num} é {Números.triplo(num)}')


