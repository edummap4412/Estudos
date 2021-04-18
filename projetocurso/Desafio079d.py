lista = []

for c in range(1, 21):
    num = int(input(f'Digite o {c}º Número:'))
    lista.append(num)
    for n in lista:
        cont = lista.count(n)
        if cont > 1:
            lista.remove(n)
print(lista)
