dados = dict()
lista = list()
soma = soma1 = 0

while True:
    dados['nome'] = str(input('Nome: '))
    resp = ' '
    while not resp in 'MF':
        resp = dados['sexo'] = str(input('[M/F]: ')).upper().strip()
        if resp not in 'MFmf':
            print('Caractere invalido')
    dados['idade'] = int(input('Idade: '))
    soma1 +=dados['idade']
    lista.append(dados.copy())
    op = ' '
    while not op in 'SN':
        op = str(input('Quer continuar? [S/N]')).upper()
        if op not in 'SN':
            print('Caracter invalido.Insira Novamente:')
    if op == 'N':
        break
print(f'Foram cadastradas :{len(lista)} pessoas')
media =soma1/len(lista)
print(f'A Média de idade de todos os cadastrados é {media}')
print('Mulheres na lista:')
for l in lista:
    if l['sexo'] == 'F':
        print(l['nome'])
print('Pessoas Mais velha:')
for l in lista:
    if l['idade'] > media:
       print(f'{l["nome"]} está acima da média de idade com {l["idade"]} ')


