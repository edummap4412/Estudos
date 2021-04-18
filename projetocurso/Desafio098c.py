def contador(i, f, p):
    if i > f:
        if p > 0:
            p *= -p
        if p == 0:
            p = 1
    cont = i
    while cont < f:
        cont += p
        print(cont, end=' ')
    print()
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo:'))

contador(ini, fim, pas)
contador(1, 10, 1)
contador(10, 1, 1)