from datetime import date
ano = date.today().year
dados = dict()
for c in range(1):
    dados['nome'] = str(input('Nome: '))
    n = int(input('Data de nascimento:'))
    resut = ano - n
    dados['idade'] = resut
    dados['CTPS'] = int(input('Número da Carteira de Trabalho(0 se não tiver):'))
    if dados['CTPS'] == 0:
        break
    else:
        dados['Contrato'] = int(input('Ano de contratação: '))
        dados['Salario'] = int(input('Qual seu Salário atual:R$ '))



print(dados)
print(aposent)
