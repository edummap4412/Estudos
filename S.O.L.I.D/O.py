"""
 Exemplo inicial  :

class Circo:

    def apresentar(self, tipo):
        if tipo == 1:
            self.aprensentar_malabarista()
        if tipo == 2:
            self.apresentar_palhaço()


    def aprensentar_malabarista(self):
        print('Maalabarista apresentando seu show')

    def apresentar_palhaço(self):
        print('Palhaço aprensentando seu show')


circo = Circo()

COMO EU IMPLEMENTEI ANTES DE VER O VIDEO :


class Apresenta():
    def apresenta(self,artista):
        return f' Nosso {artista} esta apresentando'

    def nome_artista(self,nome,funcao):
        return f'{nome},{funcao}'


class Circo(Apresenta):

    def artista(self, artista):
        super().apresenta(artista)


circo = Circo()

print(circo.apresenta('palhaço'))
print(circo.apresenta('malabarista'))
print(circo.aprentta('equilibrista'))
print(circo.nome_artista('Eduardo', circo.apresenta('malabarista')))

Solucao aplicada no video :

class Circo():

    def aprensetar(self, apresentar: any):
        apresentar.apresentar_show()


class Malabarista():

    def apresentar_show(self):
        print('Malabratista apresentando seu show')


class Palhaco():

    def apresentar_show(self):
        print('Palhaço apresentando seu Show')


class Domador():

    def apresentar_show(self):
        print('Domador apresentando seu Show')


circo = Circo()
malabarista = Malabarista()
palhaco = Palhaco()
domador = Domador()


circo.aprensetar(palhaco)
circo.aprensetar(malabarista)
circo.aprensetar(domador)


LINK : https://www.youtube.com/watch?v=XVQC1b2yPYQ
"""


