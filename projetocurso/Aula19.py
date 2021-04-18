filmes = {'Titulo': 'StarWars', 'Ano': 1977, 'Diretor': 'George Luccas'}
print(filmes.values())
print(filmes.keys())
print(filmes.items())
for k, i in filmes.items():
    print(f'{k} é {i}')

print(filmes['Titulo'])
print(filmes['Ano'])
print(f'No Ano de {filmes["Ano"]} lançou o Filme : {filmes["Titulo"]}')
print("-"*30)
for f in filmes:
    print(f)
print('-'*30)

# DICIONARIOS DENTRO DE LISTAS
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
for n in brasil:
    for c in n:
        print(f'{n["uf"]} e seu sigla é {n["sigla"]}')
print('-'*30)
pessoas1 = {'nome': 'Eduardo', 'sexo': 'M', 'idade': 24}
pessoas1['nome'] = 'Joaquina'
pessoas1['sexo'] = 'F'
pessoas1['idade'] = 22
#Além disso pode-se adicionar chaves
pessoas1['peso'] = 70.8
for k, v in pessoas1.items():
    print(f'{k} = {v}')
print('-'*30)

Estado = dict()
brasil = list()
for c in range(0, 2):
    Estado['uf'] = str(input('Unidade Federativa: '))
    Estado['sigla'] = str(input('Sigla: '))
    Estado['Ano'] = int(input('Ano de Fundação: '))
    brasil.append(Estado.copy())

for e in brasil:
    for k, v in e.items():
        print(f'O estado de {k} , {v}, foi fundada em{v}')
# Também pode-se usar :
    for v in e.values():
        print(v)

