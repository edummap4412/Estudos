soma=0
numeros = [int(input('Digite Primeiro valor')),
           (int(input('Digite Segundo valor:'))),
           (int(input('Digite Terceiro valor :')))]
for n in numeros:
    s = n**2
    soma += s
    print(f'numeros digitados foram {n}, elevados ao quadrado = {s}')
print(f'A soma entre eles é {soma}')

