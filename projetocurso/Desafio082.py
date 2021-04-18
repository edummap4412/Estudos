lista = []
par = []
impar = []
for c in range(10):
    num = int(input('Digite um Número:'))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print(lista)
print(par)
print(impar)
