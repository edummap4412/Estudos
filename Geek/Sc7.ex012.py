numero = []
t1 = 0
for c in range(1, 5):
    t2 = int(input('Digite Numero:'))
    numero.append(t2)
    for indice, n in enumerate(numero):
        t3 = numero[0]
        t1 -= numero[indice]
        print(numero[indice])
print(numero)

# ultima linha de raciocinio
# O numero na posição 0 é igual o da posição 1? (faça um programa para identificar isso )se nao or isso veja a resposta
