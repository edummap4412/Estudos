from unittest.mock import patch
from unittest import skip

from ALURA.AluraMock.livros import consultar_livros, excutar_requisicao


def test_consultar_livros_chama_obetr_url_usando_como_parametro_o_retorno_de_preparar_dados_para_requisicao():
    with patch("ALURA.AluraMock.livros.preparar_dados_para_requisicao") as duble_preparar:
        dados={'autor':'Agatha Cristie'}
        duble_preparar.return_value = dados
        with patch("ALURA.AluraMock.livros.obter_url") as duble_obter_url:
            consultar_livros('Agatha Cristie')
            duble_obter_url.assert_called_once_with("https://buscador", dados)


def test_consultar_livros_chama_executar_requisiçao_usando_retorno_obter_url():
    with patch("ALURA.AluraMock.livros.obter_url") as duble_obter_url:
        duble_obter_url.return_value = "https://buscador"

        with patch("ALURA.AluraMock.livros.excutar_requisicao") as duble_executar_requisicao:
            consultar_livros('Agatha Cristie')
            duble_executar_requisicao.assert_called_once_with("https://buscador")



def test_executar_requisicao_retorna_tipo_sting():
    resultado = excutar_requisicao("https://buscador?author=Jk+Rowlings")
    assert type(resultado) == str


