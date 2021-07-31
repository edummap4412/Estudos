lista = []
for c in range(5):
    lista.append(int(input( 'Digite Número :')))
    if lista[c] < 0:
        lista[c] = 0
print(lista)
