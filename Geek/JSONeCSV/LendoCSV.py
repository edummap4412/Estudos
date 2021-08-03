
"""
Lendo arquivos CVS - Comma Separeted Values - Valores Separados por Vigurla

# Separador por virgula

1, 2, 3, 4, 5, 6, 7, 8, 9

"geek","University", "python",

# Separador por ponto e vigula

"geek";"University"; "python";

# Separador por espaço

1 2 3 4 5 6 7 8

http://dados.gov.br/dataset

# Posivel de se trabalhar , mas não é o ideal (trabalho)

with open('lutadores.csv', encoding="utf8") as arquivo:
    dados = arquivo.read()
    print(type(dados))
    dados = dados.split(',')[3:]
    print(dados)


 A linguagem Python possui duas formas diferente para ler dados em aruivos CSV:
 - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas;
 - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDict

"""

# Reader

from csv import reader

with open('lutadores.csv', encoding="utf8") as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)# Pular cabeçalho
    for linha in leitor_csv:
        print(f'{linha[0]} nasceu em {linha[1]} e mede {linha[2]}cm ')


# DictReader
# para deteminar , caso tenho outro separador , use o delimiter

from csv import DictReader

with  open('lutadores.csv', encoding='utf8') as arquivo:
    leitor_csv = DictReader(arquivo , delimiter=',')
    for linha in leitor_csv:
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")