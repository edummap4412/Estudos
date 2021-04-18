galera = list()
pessoa = dict()
soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo']=str(input('[M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! por favor, Diite M ou F')
    pessoa['idade'] = int(input('Idade:'))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar?[S/N')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apensa S ou N')
    if resp == 'N':
        break
print('-='*30)
print(galera)
print(f'Pessoas cadastradas: {len(galera)}')
media = soma/len(galera)
print('As mulheeres cadastradas foram : ', end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print('Lista das pessoas que estão acima da média:', end=' ')
for p in galera:
    if pessoa['idade'] > media:
        print(f'{p["nome"]} tem {p["idade"]} anos.'  )
    else:
        print('Todos dentro da média de idade!')
print(f'{"VOLTE SEMPRE":.^5}')