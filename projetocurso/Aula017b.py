
'''num = [8, 7, 4, 5, 6, ]
num[2] = 7

num.insert(1, 9)
num.sort(reverse=True)
if 4 in num:
    num.remove(4)
else:
    print('Não há número 4')


print(num)'''

valores = []
valores.append(5)
valores.append(4)
valores.append(3)
for cont in range(0,5):
    valores.append(int(input('Digite um valor :')))
for c, v in enumerate(valores):
    print(f'Na posição {c} Encontrei o valor {v}')


'''a = [2, 3, 4, 7]
b = a[:]
b[2] = 5
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''
# Quando voce usa o sinal de  '='  Python  entende como uma ligaçao entere as lista ,
# por isso que se trocar um valor de uma lista a outra tambem muda .
# E usadno [:] (aula de tratamento de strings) o valor pode mudar sem que a aoutra se altere.

