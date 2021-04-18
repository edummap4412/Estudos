a=int(input('Digite um numero :'))
b=int(input('Digite segundo numero'))
c=int(input('Digite terceiro numero'))
menor= a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c
maior=a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('Valor Menor {}'.format(menor))
print('Valor Maior {}'.format(maior))
