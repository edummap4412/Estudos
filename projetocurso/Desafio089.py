lista=[]
lista2= []
media = []
while True:
    lista.append(str(input('Nome do Aluno:')))
    lista.append(int(input('Avaliação 1:')))
    lista.append(int(input('Avaliação 2:')))
    lista2.append(lista.copy())
    lista.clear()
    op =' '
    op=str(input('Quer Continuar? [S/N]'))
    if op == 'N':
        break
for indice,c in enumerate(lista2):
    notaf = (c[1] + c[2])/2
    media.append(notaf)
    print(c[1], notaf)
for ind, m in enumerate(media):
    print(f'Aluno {i} tem media {n}')




