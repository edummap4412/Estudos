def fatorial(n, show=False):
    """

    :param n: Parametro de Num
    :param show: Mostra os Valores da sequência
    :return: Retorna o valor
    """

    f = 1
    cont = n
    while cont > 0:
        f *= cont
        cont -= 1
        if show == False :
            print(cont+1, end=' ')
            print('x' if cont > 1 else '=', end=' ')
    print(f, end=' ')

num = int(input('Digite um Número:'))

fatorial(num, show=True)
