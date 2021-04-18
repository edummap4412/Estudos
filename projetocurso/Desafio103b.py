'''def ficha(jog='<Desconheido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato')


n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)'''

'''n = str(input('Número: '))
if n.isnumeric():
    print(f'{n} é número')

elif len(n) >= 2:
    print(f'{n} é uma Palavra')

else:
    print(f'{n} é uma letra')'''

m = str(input('Digite: '))

if m.isidentifier():
    print(m)
else:
    print('não é ')
