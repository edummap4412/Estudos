time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c}?')))
    jogador['gols'] = partidas.copy()
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar?[S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO!Responda apenas S ou N')
        if resp in 'N':
            break
print('-='*40)
print('cod',end=' ')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3}',end='')
    for d in v.values:
        print(f'{str(d):<15}')
    print()
print('-='*40)
while True:
    busca = int(input('Qual jogador quer mostrar?'))
    if busca > len(time):
        print('Jogador não está na lista')
    else:
        print(f'{time[busca]["nome"]}: ')
print('-='*30)
print(f'Jogador{jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador["gols"]):
    print('Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols')
