n = int(input('Digite um numero'))
if n > 0:
    n1 = n // 1000 % 10
    n2 = n // 100 % 10
    n3 = n // 10 % 10
    n4 = n // 1 % 10
    print(f'Soma de {n1, n2, n3, n4} = {n1+n2+n3+n4}')

