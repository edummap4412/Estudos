dados = dict()
quantidade = list()
comp = list()

while True:
    dados['nome'] = str(input('Nome do Jogador: '))
    dados['partidas'] = int(input('Quantas partidas jogadas: '))
    for c in range(0, dados['partidas']):
        quantidade.append(int(input(f'Quantos gols feitos na {c+1}ºPartida: ')))
    dados['gols'] = quantidade.copy()
    soma = sum(quantidade)
    dados['total'] = soma
    comp.append(dados.copy())
    quantidade.clear()
    op = str(input('Quer Continuar? [S/N]'))
    if op in 'Nn':
        break
print(quantidade)
print(comp)
print('Dados dos jogadores')
for ind, c in enumerate(comp):
    print(f'{ind} Jogador {c["nome"]} fez {c["gols"]} gols ,total:{c["total"]}')

while True:

    op = int(input('Qual opçao de jogador você quer?'))
    if op == 999:
        break
    if op > len(comp)-1:
        print(f'O jogador {op} não existe na lista.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {comp[op]["nome"]}')
        for i, g in enumerate(comp[op]["gols"]):
            print(f'Na {i+1}º partida fez {g} gols.')

