from urllib.request import urlopen


def consultar_livros(author):

    dados = preparar_dados_para_requisicao(author)
    url = obter_url("https://buscador", dados)
    ret = excutar_requisicao(url)

    return ret


def preparar_dados_para_requisicao(author):
    author = {'autor':'Agatha Cristie'}
    return  author


def obter_url(url,dados):
    url = "https://buscador"
    return url


def excutar_requisicao(url):
    with urlopen(url, timeout=10) as resposta:
        resultado = resposta.read().decode("utf-8")
    return resultado
