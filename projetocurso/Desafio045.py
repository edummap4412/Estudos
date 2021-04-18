from random import randint
from time import sleep

itens=('Pedra','Papel','Tesoura')
computador=randint(0,2)
print('''[ 1 ] Pedra [ 2 ] Papel [ 0 ] Tesoura''')

jogador= int(input('Escolha :'))
print('JO')
sleep (1)
print('KEN')
sleep(1)
print('PO!!!')
sleep (1)

print('Computador Escolheu {}'.format(itens[computador]))
print('Jogador Escolheu {}'.format(itens[jogador]))

if computador == 1:
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador Venceu')
    elif jogador == 0:
        print('Jogador Perdeu')
elif computador == 2:
    if jogador == 1:
        print('Jogador Perdeu')
    elif jogador == 2:
        print('EMPATE')
    elif jogador == 0:
        print('Jogador Vence')
elif computador == 0:
    if jogador == 1:
        print('Jogador Vence')
    elif jogador == 2:
        print('Jogador Perde')
    elif jogador == 0:
        print('EMPATE')




