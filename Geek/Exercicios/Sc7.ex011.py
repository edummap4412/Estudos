vetor =[]
c = cont = s = 0
while not c == 10:
    c += 1
    vetor.append(int(input('Digite os números:')))
for n in vetor:
    if n < 0:
        cont += 1
    else:
        if n > 0:
            s += n
print(f'Quantidade de números negativos é {cont}')
print(f'A Soma dos números positivos é {s}')
