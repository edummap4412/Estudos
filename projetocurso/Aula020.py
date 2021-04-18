
def titulo(txt):
    print('-='*30)
    print(txt)

titulo('Testando')
titulo('Evoluindo')
titulo('Sucesso')

def soma(a, b):
    s = a + b
    print(s)

for c in range(1):
    n= int(input('Digite primeiro numero:'))
    n2 =int(input('Digite segundo numero :'))

    print(soma(n, n2))

#Desempacotamento
def contador(*num):
    tam = len(num)
    print(f'Racebi :{num} e sao ao todo :{tam} números', )



contador(2, 3, 4, 5, 6)
contador(3, 4, 5, 6, 7)
contador(3, 4, 4, 5, 6, 7)

#Maneira com  lista
def dobra(lst):
    pos = 0
    while pos <len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 4, 6, 7, 8, 9]
print(valores)
dobra(valores)
print(valores)
