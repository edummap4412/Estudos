def contagem_de_caracteres(s):
    """Funcão que conta os caracters de uma string

    >>> contagem_de_caracteres('Eduardo')# Ctrl + Shift + J para subir as linhas
    {'E':1, 'd':1, 'u':1, 'a':1, 'r':1, 'd':1, 'o':1}
  """
    resultado = {}

    for caracter in s:
        contagem = resultado.get(caracter,0 )
        contagem += 1
        resultado[caracter] = contagem
    return resutaldo

if __name__ == '__main__':
    contagem_de_caracteres('Eduardo')
    print()
    contagem_de_caracteres('Banana')
