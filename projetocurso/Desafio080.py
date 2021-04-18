lista = []
for c in range(0, 5):
    num = int(input('Número:'))
    lista.append(num)
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
            lista.insert(0, num)
        if maior < num > menor:


print(lista)
print(maior)
print(menor)
