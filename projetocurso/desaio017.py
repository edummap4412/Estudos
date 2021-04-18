'''from math import hypot
n=float(input(" digite o valor do cateto adjacente :"))
n1=float(input('Digite o valor do cateto oposto :'))
print(' Valor da hipotenusa é {:.2f}'.format(hypot(n,n1)))'''


from math import sqrt
n=float(input('digite valor do hipotenusa:'))
n1=float(input('digite o valor do cateto adjacente :'))
c=(n**2)-(n1**2)
a=(c**2)-(n**2)
print('Valor do cateto oposto é de {:.2f}'.format(sqrt(c)))
print('Valor do cateo adjacente é de {}'.format(sqrt(a)))







