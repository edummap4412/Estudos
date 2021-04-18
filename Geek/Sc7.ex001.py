A = [1, 0, 5, -2, -5, 7]
soma = 0
for indice, n in enumerate(A):
    n1 = A[0]
    n2 = A[1]
    n3 = A[5]
    A[4] = 100
    print(f'{indice} , {n:> 3}')
print(f'Soma é {n1+n2+n3}')
print(A)
print(soma)
