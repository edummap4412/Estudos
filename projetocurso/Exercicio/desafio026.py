frase=str(input('Digite um frase')).strip()
frase1=frase.upper()
frase2=len(frase1)
print('A letra a aparace {} vazes na frase'.format(frase1.count('A')))
print( ' A primeira letra  R apareceu na posição {}'.format(frase1.find('R')))
print('A ultima letra R aparece na posição {}'.format(frase1.rfind('R')))
if frase2 >= 24:
    print( 'Nome Grande!')
else:
    print('Nome Pequeno')


'''frase=str(input('Digite seu nome :')).upper()
print('A letra a aparece na frase {} vezes'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')))
print('A ultima letra A aparece na posição {}'.format(frase.rfind('A'))'''


