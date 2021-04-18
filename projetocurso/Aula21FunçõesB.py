"""
dados = list()
dados2 =list()
dic =dict()
def listas (a,b):
    dic['id'] : a
    dic['age']: b
    dados.append(dic)
    dados2.append(dados)
    dados.clear()
    print( a,b)

for c in range(3):

    nome = str(input('Nome: '))
    idade = int(input('Idade: '))

    listas(nome,idade)
print(dados2)

"""

# Passando uma lista para uma Função
"""

def listas(nomes):
    for nome in nomes:
        print(f'Olá, {nome}, Prazer em conhecer')


grupo = {}
for c in range(3):
    grupo.append(str(input('Nome: ')))
    grupo.append(int(input('Idade: ')))
listas(grupo)
"""
"""
#Modificando uma lista em uma função

#Programa usando so lista:
design_pendente = ['capa de Iphone', 'parte de Robô', 'Decoração']
design_feitos = []

while design_pendente:
    design_atual = design_pendente.pop()# Pode parar um lopping while com um pop de listas

    print(f'Mostrador de Modelos:{design_atual}')
    design_feitos.append(design_atual)

print("\n Estes foram os modelos fabricados: ")
for design_feitos in design_feitos:
    print(design_feitos)"""

#Programa usando Funções:
"""
def print_models(design_pendente,design_completos):
    while design_pendente:
        design_atual = design_pendente.pop()

        print(f'Mostrando os Modelos:{design_atual}')
        design_completos.append(design_atual)

def mostre_design_completos(design_completos):
    print('\n Estess são os Design completos:')
    for design_completo in design_completos:
        print(design_completo)


design_pendente = ['Pelicula para celular', 'Carregador','Fones de Ouvido']
design_completos = []

print(design_pendente, design_completos)
mostre_design_completos(design_completos)
"""
lista =[1, 2, 4, 5]
lista2 = []

while lista:# Enquanto lista for verdadeiro
    lista3 = lista.pop()
    lista2.append(lista3)
print(lista2)
