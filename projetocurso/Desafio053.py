cont=0
cont1=0
maior=0
from datetime import date
ano= date.today().year

for c in range (1,6):
    data=int(input('Digite um data de nascimento :'))
    data1=ano-data
    if data1>=21:
        cont+=1
        if  c == c:
            if data1>maior:
                maior=data1

    elif data1 <=20:
        cont1+=1
print('Temos {} maiores de idade\n Temos {} menores de idade'.format(cont,cont1))
print('Mais velho tem {} anos'.format(maior))



