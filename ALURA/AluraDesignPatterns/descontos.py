class Desconto_por_cinco_itens():

    def __init__(self,proximo_desconto):
        self.proximo_desconto = proximo_desconto


    def calcula(self, orcamento):

        if not orcamento.total_item >= 5:
            return orcamento.valor * 0.1
        return self.proximo_desconto.calcula(orcamento)


class Desconto_por_mais_de_quinhentos_reais():

    def __init__(self, proximo_desconto):
        self.proximo_desconto = proximo_desconto

    def calcula(self, orcamento):
        range = 500

        if not orcamento.valor >= range:
            total_desc = orcamento.valor * .07
            return total_desc
        return self.proximo_desconto.calcula(orcamento)


class Desconto_por_peso():
    def __init__(self, proximo_desconto):
        self.proximo_desconto = proximo_desconto

    def calcula(self, orcamento):
        if orcamento.peso >= 7:
            print(orcamento.peso)
            return orcamento.valor * .05


class Sem_desconto():

    def calcula(self):
        return 0
    