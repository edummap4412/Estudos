from datetime import date
nas=int(input('Digite seu ano de nascimento :'))
ano=date.today().year
sub=2021-nas
print('Sua idade é de {} anos '.format(sub))
if nas<=1995:
    print('Categoria MESTRE')
elif  nas==1996 or nas<=2000 :
    print(' Sua categoria é SENIOR')
elif nas ==2002 or nas<=2006 :
    print('Sua categoria é JUNIOR')
elif nas ==2007 or nas<=2011:
    print('Sua categoria é INFANTIL')
elif nas ==2012 or nas<=2018:
    print('Sua é Mirim')






















