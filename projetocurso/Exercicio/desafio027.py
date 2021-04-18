'''frase=str(input('Digite seu nome :')).strip().upper()
frase1=frase.split()
print('Seu primeiro nome é {}'.format(frase1[0]))
print('Seu ulltimo nome é {}'.format(frase1[len(frase1)-1]))
print('Quandtidae de  caracteres {}'.format(len(frase)-frase.count(' ')))
print(' a ultima letra do nome é {}'.format(frase.rfind('A')))'''


frase=str(input('Digite seu nome :')).strip().upper()
frase1=frase.split()

print( 'Posição do ultimo M é {}'.format(frase.rfind('M')-frase.count(' ')))

print('Quantidade de caracters é de {}'.format(len(frase)-frase.count(' ')))
print('Ultimo palavra da frase é {}'.format(frase1[len(frase1)-1]))




















