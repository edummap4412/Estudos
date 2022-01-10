import unittest

from ALURA.AluraDesignPatterns.orcamento import Orcamento, Item


class Test_calculo_de_imposto(unittest.TestCase):

    def setUp(self):
        super(Test_calculo_de_imposto, self).setUp()
        orcamento = Orcamento()

        orcamento.adciona_item(Item('PlayStation', 1830, 50))
        orcamento.adciona_item(Item('XboxOne', 2030, 30))
        orcamento.adciona_item(Item('NintendoWiiU', 2330, 40))

    def test_retorna_nome_do_item(self):

        item = Item('PlayStation', 2000, 40)
        orc = Orcamento()
        orc.adciona_item(item)
        print(item.nome)
        print(orc.obter_itens)

