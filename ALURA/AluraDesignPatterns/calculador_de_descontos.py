from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Desconto_por_peso, Sem_desconto
from orcamento import Orcamento, Item


class Calculador_de_descontos():

    def calcula(self, orcamento):

         desconto = Desconto_por_cinco_itens(
             Desconto_por_mais_de_quinhentos_reais(
                 Desconto_por_peso(Sem_desconto)
             )).calcula(orcamento)

         return desconto


orcamento3 = Orcamento()
orcamento3.adciona_item(Item('PlayStation', 1830, 50))
orcamento3.adciona_item(Item('XboxOne', 2030, 30))
orcamento3.adciona_item(Item('NintendoWiiU', 2330, 40))
orcamento3.adciona_item(Item('NintendoWiiU', 2330, 40))
orcamento3.adciona_item(Item('NintendoWiiU', 2330, 40))
orcamento3.adciona_item(Item('NintendoWiiU', 2330, 40))

print(orcamento3.total_item())
print(orcamento3.obter_itens)
calculados = Calculador_de_descontos()

descontos_calculado3 = calculados.calcula(orcamento3.valor)

print(descontos_calculado3)


