from math import trunc
print('-'*20)
print('Analisando Triangulo')
print('-'*20)
a=float(input('Valor reta 1 :'))
b=float(input('Valor reta 2 :'))
c=float(input('Valor reta 3 :'))
if a< b + c and b <a + c and c<a + b:
    print('com essas medidas faz um triangulo ,PARABÉNS'.format(a,b,c))

else:
    print('Com essas medidas não há um triangulo')







