dados = []
dados2 = []
while True:
    dados.append(str(input('Nome :')))
    dados.append(float(input('Peso: ')))
    dados2.append(dados.copy())
    dados.clear()
    op =' '
    while not op in 'SN':
        op = str(input('Quer continuar? [ S/N ]')).strip().upper()
    if op == 'N':
        break
print(dados2)
print('Pessoas acima do Peso:')
for n in dados2:
    if n[1] >= 80:
        print(f'{n[0]}', end=' ')
print()
print('Pessoas abaixo do Peso:')
for n in dados2:
    if n[1] <= 60:
        print(f'{n[0]}', end=' ')
    else:
        print('Não pessoas abaixo do Peso')

