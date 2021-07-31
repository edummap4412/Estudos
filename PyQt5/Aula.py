import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton, QToolTip


class Janela (QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo ="Primeiro Janela"

        botao1 = QPushButton("Botao 1",self)
        botao1.move(150, 200)
        botao1.resize(150, 80)
        botao1.setStyleSheet('QPushButton {background-color:')
        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()


aplicacao = QApplication(sys.argv)
j= Janela()
sys.exit(aplicacao.exec_())
