'''dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])
pessoas = list()
pessoas.append(dados[:])'''

# Deep copy e Shalow copy
''''dados = list()
dados.append('Eduardo')
dados.append(27)
pessoas = list()
pessoas.append(dados[:])
dados[0] = 'Maria'
dados[1] = 25
pessoas.append(dados)
print(pessoas)'''''

'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0])
print(galera[0][0])
print(galera[2][1])
for p in galera:
    print(f'{p[0]:.<30}',end='')
    print(f'{p[1]:.>10}')'''
galera = list()
dado = list()
maior = menor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'Nome da pessoa é {p[0]}')
        maior += 1
    else:
        print(f'Nome dos menores de idade é {p[0]}')
        menor += 1
print(f'Temos {maior} Maiores e {menor} Menores')
print(galera)
