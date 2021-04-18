resp = []
respaluno = []
respaluno2 = []
nome = []
soma = 0
print('Gabarito da Prova')
for c in range(0, 5):
    resp.append((str(input(f'Questão {c}: '))))
print(resp, end='')
print()
print('------------------')
print('Respostas do Aluno: ')
print('------------------')

while True:
    nome = str(input('Nome: '))
    respaluno.append(nome)
    for c in range(5):
        questao = str(input('Questões:'))
        respaluno.append(questao)
        if c >= 4:
            respaluno2.append(respaluno.copy())
            respaluno.clear()
    op =' '
    op =str(input("Quer continuar? [S/N]"))
    if op == 'N':
        break
print(respaluno2)
print(respaluno)
for c in range(5):
    print(resp[c])
for n in respaluno2:
    print(n)
