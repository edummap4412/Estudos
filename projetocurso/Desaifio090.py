form = dict()
form['nome'] = str(input('Nome: '))
form['media'] = float(input('Média: '))
if form['media'] < 5.9:
    form['situação'] = 'Reprovado'
else:
    form['situação'] = 'Aprovado'
print(f'O aluno {form["nome"]} foi {form["situação"]} com média {form["media"]}')
