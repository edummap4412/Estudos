vetor = []

while True:
    for c in range(1, 6):
        vetor.append(int(input('Digite Número :')))
    print('''OPÇÕES:
    [ 1 ] Imprime o vetor em ordem direta
    [ 2 ] Imprime o vetor em ordem inversa
    [ 0 ] Sair''')

    op = int(input('Escolha Opção'))
    if op == 0:
        break
    else:
        if op == 1:
            print(vetor)
            break
        if op == 2:
            vetor.reverse()
            print(vetor)
            break
