vetor = []
c = 0
while not c == 15:
    c += 1
    vetor.append(float(input(f'Digite {c}º número:')))
    s=sum(vetor)
print(f'Soma das notas é {s} .Media geral da classe é {s/c}')
