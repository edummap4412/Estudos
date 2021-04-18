
from datetime import date
ano=int(input('Digite um ano :'))
if ano==0:
    ano=date.today().year
if ano%4==0 and ano%100 or ano%400 ==0:
    print('Ano é Bissexto {}'.format(ano))
else:
    print('Ano não é Bissexto {}'.format(ano))

#and = para dar mais uma condição
# != Diferente
# == = igual
# or =  ou


