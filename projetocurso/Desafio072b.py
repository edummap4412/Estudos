numeros=('zero','um','dois','tres','quatro','cinco','seis',
         'sete','oito','nove','dez','onze','doze','treze',
         'catorze','quinze','dezesseis','dezessete','dezoito',
         'dezenove','vinte')


while True:
    contagem=int(input('Digite um número de 0 a 20:'))
    if 0<= contagem <=20:
        break
    print(f'Você digitou o número {numeros[contagem]} ')
    op=' '
    while not op in 'SN':
        op=str(input('Você quer continuar? }'))