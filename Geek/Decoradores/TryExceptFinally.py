""" Try deixa voce testar o bloco de codigos para erro
    Caso de Erros Except lida com os erros

    Finally Excuta o codigo independente do resultado de Try e Except.

try:
    x = 3 + '9'
    print(x)
except NameError:
    print("ocorreu um erro")

except TypeError:
    print("Alguma coisa chegou errada"


" Se estirver tudo certo no try . Else vai mostrar a mensagem dizendo que nao houve erros"
try:
    print("Hello")
except:
    print("Something went wrong")

else:
    print("Nothing went wrong")
# Finally

try:
    print('Sucess')
except:
    print("Something went wrong")
finally:
    print("the 'try except' is finished")

"""

from _csv import writer
import pprint
with open('demofile.csv','a', encoding='utf8') as arquivo:
    f_csv = writer(arquivo)
    f_csv.writerow(['Nome', 'Gênero', 'Duração'])
    filme = ' '
    try:
        while filme != 'sair':
            filme = str(input('Informe o nome do filme: '))
            if filme != 'sair':
                genero = str(input( 'Informe o gênero: '))
                duracao = int(input('Informe a duração (em minutos): '))
                f_csv.writerow([filme, genero, duracao])
    except:
        print('erro no tipo da variavel')


with open('arquivo.csv','a',encoding='utf8') as arquivo:
    doc_csv = writer(arquivo)
    doc_csv.writerow(['Nome','Sexo','Idade'])
    nome = ' '
    try:
        while nome !='sair':
            nome = str(input('Digite seu nome (digite "sair" para sair):'))
            sexo = str(input('Informe o Sexo: '))
            idade = str(input('Informe a idade:'))
            doc_csv.writerow([nome,sexo,idade])
    except:
        print("Erro no tipo da variavel")

