dados = dict()
dados['nome'] = str(input("Nome: "))
dados['media'] = int(input('Média: '))
if dados['media'] <= 5.9:
    dados['situação'] = 'Reprovado'
else:
    dados['situação'] = 'Aprovado'
for k, v in dados.items():
    print(f'{k} : {v}')
