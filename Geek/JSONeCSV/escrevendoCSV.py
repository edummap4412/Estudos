"""

Escrevendo em arquivos CSV

reader()
writer()


writerow() -> Escreve uma linha

"""
from _csv import writer
from csv import DictWriter

with open('filmes.csv', 'w', encoding='utf8') as arquivo:
    escritor_csv = writer(arquivo)
    filme = ' '
    escritor_csv.writerow(['Título', 'Genero','Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])


# DictWriter


with open('filmes2.csv', 'w', encoding='utf8') as arquivos:
    cabecalho = ['Titulo',' Genero','Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('informe Genero: ')
            duracao = input('informe Duração: ')

        escritor_csv.writerow({"Titulo": filme, 'Genero': genero, "Duração": duracao})