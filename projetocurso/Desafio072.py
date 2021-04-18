numeros=('zero','um','dois','tres','quatro','cinco','seis',
         'sete','oito','nove','dez','onze','doze','treze',
         'quatorze','quinze','dezesseis','dezessete','dezoito',
         'dezenove','vinte')

contagem=int(input('Digite um Número :'))

while True:
    while contagem in 0*20:
        contagem=int(input('Número fora do "Range" .Digite novamente:'))
    print(f' Você digitou o número {numeros[contagem]}')
    op=' '
    while not op in 'SN':

        op=str(input('Quer continuar ? [S / N]')).strip().upper()

    if op == 'S':
        contagem=int(input('Digite outro número:'))
    if op== 'N':
        break

