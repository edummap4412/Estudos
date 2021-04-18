lista = []
princ = []

while True:
    lista.append(str(input('Nome: ')))
    lista.append((int(input('Avaliação1: '))))
    lista.append((int(input('Avaliação2: '))))
    princ.append(lista.copy())
    lista.clear()
    op = str(input('Quer Continuar? [S/N]'))
    if op in 'N':
        break
print(princ)

for ind, p in enumerate(princ):
    media = (p[1] + p[2])/2

    print(f'Nº   Nome   Nota\n{ind:},{p[0]:.^5} {media}')

while True:
    numero = int(input(' Digite numero do aluno para informações da Nota:'))
    if numero > len(princ):
        print('Aluno não existe.Digite Novamente')
    if numero == 999:
        break
    print(princ[numero])


