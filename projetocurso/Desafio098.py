def titulo():
    print('-='*30)

def cont2 (d, e):
    for c in range(d, e, -1):
        print(c, end=' ')
    print()

d = 10
e = 1
cont2(d, e)
titulo()
def cont1 (d, e):
    for c in range(d, e):
        print(c, end=' ')
    print()
d = 1
e = 10
cont1(d, e)
titulo()
def cont(a, b, c):
    for c in range(a, b, c):
        print(c, end=' ')
    print()

n = int(input('Inicio:'))
n1 = int(input('Fim: '))
n2 = int(input('Passo:'))
if n > n1:
    if n2 > 0:
        n2 = -n2
    if n2 == 0:
        n2 = 1
cont(n, n1, n2)
titulo()
