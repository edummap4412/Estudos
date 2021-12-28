from lista_imposto import ISS

class Calculador_de_impostos():

    def __init__(self, orcamento):
        self.orcamento = orcamento

    def realiza_calculo(self, orcamento, impostos):

        impostos_calculado = impostos.calcula(orcamento)

        return impostos_calculado

