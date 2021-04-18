from math import pow, ceil

peso = float(input('Qual seu peso ?'))
altura = float(input('Qual sua altura ?'))
imc = peso / (altura * altura)
print('Seu IMC é {:.1f}'.format(imc))
if imc<=18.4:
    print('Desnutrido')

elif imc >= 18.5 and imc < 24.9:
    print('Normal')
elif imc <= 25 and imc < 29.9:
    print('Sobrepeso')

elif imc >= 30 and imc < 39.9:
    print('OBESIDADE')
else:
    print('OBESIDADE GRAVE')
