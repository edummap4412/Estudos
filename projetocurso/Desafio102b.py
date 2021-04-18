n = int(input('Número: '))
f = 1
cont = n
while cont != 0:
    f *= cont
    cont -= 1

    print(cont+1, end=' ')
    print('x'if cont > 0 else '=',end=' ')
print(f, end=' ')
