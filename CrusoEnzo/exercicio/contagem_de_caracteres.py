def contagem_de_caracteres(s):
    """Funcão que conta os caracters de uma string

    >>> contagem_de_caracteres('Eduardo')
    E:1
    d:1
    u:1
    a:1
    r:1
    d:1
    o:1
    >>> contagem_de_caracteres('Banana') # ctrl + D duplica caracters e crtl + shift (sobe) caracteres
    B:1
    a:1
    n:1
    a:1
    n:1
    a:1
    :param s:  String para contar

    """
    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:

            contagem += 1
        else:
            print(f'{caracter_anterior} :{contagem}')
            caracter_anterior = caracter
            contagem = 1
    print(f'{caracter_anterior} :{contagem}')


if __name__ == '__main__':
    contar_caracteres('Eduardo')
    print()
    contar_caracteres('Banana')
