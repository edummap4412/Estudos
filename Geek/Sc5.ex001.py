maior=0
menor=0
numeros = int(input('Digite Primeiro número'))
numeros2 = int(input('Digite Segundo número:'))
'''for n in numeros:
    print(n)
print(f'Maior é {max(numeros)}')
print(f'Menor é {min(numeros)}')'''

if maior > numeros:
    maior = numeros
    menor = numeros2
    print(f'Maior é {numeros}\n Menor é {numeros2}')
else:
    print(f'Maior é {numeros2}\n Menor é {numeros}')
