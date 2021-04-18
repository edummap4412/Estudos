num = list()
par = list()
impar = list()
while True:
    num.append(int(input('Digite Número:')))
    op = str(input('Quer Continuar? [S/N]'))
    if op in 'N':
        break
for indice, n in enumerate(num):
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        impar.append(n)

print(num)
print(par)
print(impar)

