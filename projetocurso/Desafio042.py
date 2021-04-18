a=int(input('Digite um valor :'))
b=int(input('Digite outro valor :'))
c=int(input('Diite outro valor :'))
if a<b+c and b<a+c and c<b+a :
    print('Forma um triangulo')
    if a== b == c:
        print( 'EQUILATERO')
    elif a != b !=c !=a:
        print('ESCALENO')
    else:
        print('isosceles')
else:
        print('Nao é triangulo')
#n if dentro de outro if é usado numa condiçao quando temos condicçoes de ser ou nao ser . quando isso ocorre é indicado esse metodo












