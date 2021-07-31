maior = 0
menor = 0

for c in range(4):
    n = int(input('Digite um número :'))
    if c == 0:
        maior = n
        menor = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
print(f'{maior}')
print(f'{menor}')
