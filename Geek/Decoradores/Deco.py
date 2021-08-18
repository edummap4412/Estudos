""" Decorador realiza um processo com uma função decorada  e devolve ou substitui " \
por um invocavel ( calllable) ou outro objeto

@decorate
def target():
    print('running target()')
 é o mesmo que escrever:

 def target():
    print('running target()')

    target = decorate(target)
registro = []

Exemplo 2 (7.2 na apostila)
def register(func):
    print('running register(%s)' % func)
    registro.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registro)
    f1()
    f2()
    f3()


if __name__ =='__main__':
    main()
"""

