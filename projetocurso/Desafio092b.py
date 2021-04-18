from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
idade = datetime.now().year - nasc
dados['idade'] = datetime.now().year - nasc
dados['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = (dados['contratação'] + 35) - nasc
print(dados)
for k, v in dados.items():
    print(f'{k} : {v}')
