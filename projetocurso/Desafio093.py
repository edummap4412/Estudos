dados = {}
quantidade = []
soma = 0
dados['nome'] = str(input('Nome: '))
dados['Partidas'] = int(input('Partidas Jogadas: '))
for c in range(0, dados['Partidas']):
     quantidade.append(int(input(f'Quantos gols na {c+1}º:')))
     dados['gols'] = quantidade
print('-='*30)
print(dados)
print('-='*30)
for ind, q in enumerate(quantidade):
    print(f'Na {ind+1}ºPartida,o Jogador {dados["nome"]} fez {q} gols')
    soma += q
    dados['total'] = soma
print(f'Total foi de {soma} gols')
