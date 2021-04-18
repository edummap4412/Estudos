def dobro(num, show=False):

   if show:
    return f'R${num * 2}'
   else:
    return num * 2


def aumento(num):
    return num * 1.10


def diminuir(num):
    return num - (num * 0.13)


def mostra (num):
        return f'R${num}'


def metade(num):
    return num / 2


def formato(show=False):
    if show:
        return f'R${num}'

def resumo(num,a,b):
    dados= dict()
    print('~'*30)
    print(f'{"RESUMO DA LISTA":^30}')
    print('~'*30)
    dados['metade'] = num / 2
    dados['dobro'] = num * 2
    dados['aumento'] = num + (a/100*num)
    dados['diminui'] = num + (b/100*num)
    for k, v in dados.items():
        print(f'{k}: {v:>20}')
    print()
    return dados
