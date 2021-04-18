def fatorial(n):
    f = 1
    for c in range(0, n, -1):
        f *= n
        return f


num = int(input('Digite um valor:'))
fat = fatorial(num)
print (f'O fatorial de {num} é {fat}')