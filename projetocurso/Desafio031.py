'''n=int(input('Qual as distancia da viagem em KM :'))
n1=n*0.50
n2=n*0.45
if n<=200:
    print('valor da passagem é R${}'.format(n1))
else:
    print('valor da passagem é R${:.2f}'.format(n2))
print('Obrigado pela preferencia')'''
# Ou
n=float(input('Qual a distancia da sua viagem em KM'))
print(n*0.50if n<=200else n*0.45)
print(' Valor da viagem é R${:.2f}'.format(n))






