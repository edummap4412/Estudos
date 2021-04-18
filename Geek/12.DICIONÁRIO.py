'''
Dicionários ( dict)
OBS:Em algumas linuaguens de programação , os dicionarios Python são conhecidos por Mapas

Dicionarios são coleções do tipo ''chave : valor.''
-Dicionarios são representados por Chave "{}"
'''
# Forma mais comum de criação
paises = {'br':'Brasil', 'eua': 'Estados Unidos', 'py':'Paraguai'}
print(paises)
print(type(paises))

# Forma 2 menos comum

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

# Acessando elementos

#Forma - Acessando via  chave :
print(paises['br'])
print(paises['eua'])

#Acessando via get - Recomendada
print(paises.get('br'))
print(paises.get('eua'))
print(paises.get('ru'))

# Podemos definir valor padrao se nao achar a chave informada
pais = paises.get('br', 'Desconhecido')

print(f'Encontrei o pais {pais}')
# Quando usar 'in' para encontrar valores .No caso do dict ele le as CHAVES :

#Exemplo

print('br' in paises)# <- Chave
print('Paraguai' in paises)# <- Valor

if 'ru' in paises:
    russia = paises['ru']

#Podemos utilizar qualquer tipo de dado (int, float,string,boolean),inclusive list , tuple , dict,
# como chaves de dicionaiorios

localidades = {
    (35.6895,39.6917):'Escritório em Tokio',
    (40.7128, 74.0060):'Escritório em Nova York',
    (37.7749, 122.4194): ' Escritório em São Paulo',}
print(localidades)

#Adicionar elementos em um dicionário

receita = {'jan':100, 'fev':120, 'mar':300 }
print(receita)

receita['Abr'] = 350

print(receita)

# Forma 2

novo_dado ={'mai':400}

receita.update(novo_dado)

print(receita)

#Atualizar Dados

#Forma 1
receita['mai'] = 550

print(receita)

#Forma 2
receita.update({'mai':600})

print(receita)

'''
Em dict NÃO pode ter CHAVE repetidas'''

# Como Remover dados de um dicionaio: Método mais comum
receita1 ={'jan': 300, 'fev': 400, 'mai': 600}
ret=receita1.pop('mai')
print(receita1)
#OBS : Aqui precisamos SEMPRE informar a chave.

#Retorna o valor removido
print(ret)

#Forma 2
# Não retorna valor
del receita1['fev']
print(receita1)

# Imagine que você tem um comercio eletronico, onde temos um carrinho de compras na qual adicionamos produtos.
'''
Carrinho de compras:
        Produto 1
            - nome
            - quantidade
            - valor
        Produto 2
            - nome
            - quantidade
            - valor
            
'''

#Podemos fazer com listas ? sim
carrinho = []

produto1 = ['PlayStation 4', 1, 2300.00]
produto2 = ['Tv Lcd 50', 1, 1800.00]

carrinho.append(produto1)
carrinho.append(produto2)
print(carrinho)

#Podemos Fazer com Tuplas ? sim

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('Tv Lcd 50', 1, 1800.00)
carrinho = produto1 + produto2
print(carrinho)

#Produto no Dicionario :

carrinho = []

produto1 = {'nome':'PlayStation4', 'quandtidade':1, 'valor': 2300.00}
produto2 = {'nome': 'Tv Lcd 50', 'quantidade': 1, 'valor': 1800.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
#Desta forma adicionamos ou removemos produtos no carrinho e em cada produto
#podemos ter a certeza sobre cada informação

#Metodos Dicionario:
d = dict(a= 1, b=2,c=3)

#limpar

'''d.clear()
print(d)'''

#copiar

#forma1
novo = d.copy()#Deep Copy(muda só na usada)
novo = d # Shallow copy ( muda em ambas )
novo['d'] = 4
print(d)

print(novo)
# Forma não usual de Criaçao de dicionarios
outro = {}.fromkeys('a', 'b')
print(outro)

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))
# O método fromkeys recebe dois parÂmetros: um iterável e um valor.
#Ele vai gerear para cada valor do iteravel uma chave e ira atribuir a esta chave o valor informado
#nao exista

veja ={}.fromkeys('teste','valor')#<- não repete os ultimos caracteres pois em Dict nao repete valor
print(veja)

veja = {}.fromkeys(range(1, 11),'novo')
print(veja)
