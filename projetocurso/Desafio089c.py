ficha = list()
while True:
    nome = str(input('Nome : '))
    nota1 = float(input('Avaliação1: '))
    nota2 = float(input('Avaliação2: '))
    media = (nota1+nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    resp =' '
    resp =str (input('Quer continuar? [S/N]'))
    if resp in 'N':
        break
print(f'{ficha}')
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print("-"*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    opc = int(input('Mostrar notas de qual aluno?(999 interrompe)'))
    if opc == 999:
        print('FINALIZANDO')
    if opc <= len(ficha)-1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')

