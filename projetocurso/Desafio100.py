from random import randint
lista = []
lista1 = []
tot = 0
m = int(input('Quando números voce conjuntos  precisa ?'))
q = int(input('Qual quantidade de de números que você precisa?'))
while tot <= m-1:
    def somaPar(ls1):
        soma = 0
        for n in ls1:
            if n % 2 == 0:
                soma += n
        print(f'Soma dos números pares é {soma}.')

    def cont(lst):
        lst.clear()
        for c in range(q):
            lst.append(randint(1, 10))

        print(f'Números escolhidos foram :{lst}')
    tot += 1

    cont(lista)
    somaPar(lista)
