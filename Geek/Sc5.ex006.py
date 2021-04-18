'''alhar = 0
peso = float(input('Seu Peso :'))
ideal = float(input('Digite o peso que deseja atingir:'))

while peso > ideal:
    peso = malhar + peso

print(peso)'''

malhar = 0
idade=int(input('Idade :'))
peso = float(input('Seu Peso :'))
ideal = float(input('Digite o peso que deseja atingir :'))

while True:
    if peso > ideal:
        malhar += 1
        vezes = peso - malhar
        if vezes == ideal:
            break
print(f' para alcançar o peso desejado de {vezes} voce precisa malhar {malhar} vezes')
