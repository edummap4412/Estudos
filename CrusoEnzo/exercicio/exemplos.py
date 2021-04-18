


def cont(s):
    a={'E': 1, 'D': 2, 'U': 3}
    dados = {}
    for caracter in s:
        contagem = dados.get(caracter, 0)
        contagem += 1
        dados[caracter] = contagem

    return dados

    print(cont(dados))
