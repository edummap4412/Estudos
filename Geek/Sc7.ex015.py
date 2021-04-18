#é uma Forma d de fazer porém a um bug onde nao elimina todos os numeros repetidos
'''vetor = []
vetor1 = []
for n in range(20):
    t1 = int(input('Digite um número:'))
    vetor.append(t1)
    vetor1.append(t1)
    cont = vetor.count(t1)
    print(cont)
    if cont > 1:
        vetor1.pop(t1)
print(vetor)
print(vetor1)'''

vetor = []
for c in range(20):
    vetor.append(int(input('Número:')))
print(vetor)
print(sorted(set(vetor)))
print(sorted(vetor))
