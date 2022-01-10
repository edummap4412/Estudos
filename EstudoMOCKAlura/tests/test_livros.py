import unittest

from EstudoMOCKAlura.colecao.livros import consultar_livros
from unittest.mock import patch
from unittest import skip


class TestandoLivros(unittest.TestCase):

    def test_consultar_livros_retornar_resultado_froamdo_string(self):
        resultado = consultar_livros("Agatha Christie")
        assert type(resultado) == str


    def test_consultar_livros_chamar_preparar_dados_para_requisicao_uma_vez_e_com_os_mesmos_parametros_de_consultar_livro(self):
        with patch("EstudoMOCKAlura.colecao.livros.preparar_dados_para_requisicao") as duble:
            consultar_livros("Agatha Christie")
            duble.assert_called_once_with("Agatha Christie")

    def test_consultar_livros_chama_obter_url_usando_como_parametro_o_retorno_de_preparar_dados_para_requisicao(self):
        with patch('EstudoMOCKAlura.colecao.livros.preparar_dados_para_requisicao') as duble_preparar :

            dados= {"autor": "Agatha Christie"}
            duble_preparar.return_value = dados
            with patch("EstudoMOCKAlura.colecao.livros.obter_url") as duble_obter:
                consultar_livros("Agatha Christie",dados)
                duble_obter.assert_called_once_with("https://buscador", dados)

    def test_consultar_livros_chama_executar_requisicao_usando_retorno_obter_url(self):
        with patch('EstudoMOCKAlura.colecao.livros.executar_requisicao') as duble_executar_requisicao:
            consultar_livros("Agatha Christie")
            duble_executar_requisicao.assert_called_once_with("https://buscador")