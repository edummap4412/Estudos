
def consultar_livros(autor,dados=None):
    preparar_dados_para_requisicao(autor)
    obter_url("https://buscador", dados)
    executar_requisicao('https://buscador')
    return ""


def preparar_dados_para_requisicao(autor):
    pass


def obter_url(url,dados):
   pass


def executar_requisicao(url):
    pass
