class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def nome(self, nome2):
        self.__nome = nome2

    def idade(self, idade2):
        self.__idade = idade2

    def altura(self, altura2):
        self.__altura = altura2

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_altura(self):
        return self.__altura

    def imprimir(self):
        return f"{self.__nome} tem {self.__altura} e {self.__altura}" \
               f"anos "


idadee = alturaa = cad = ''
listacad = []
while cad != 'N':
    cad = str(input("Deseja cadastrar um indíviduo [S/N] ")).upper()
    if cad in 'Ss':
        nomee = str(input("Digite o nome da pessoa "))
        try:
            idadee = int(input("Digite a idade da pessoa "))
        except (TypeError, ValueError):
            print("Idade tem que ser número inteiro")
            break
        try:
            alturaa = float(input("Digte a altura da pessoa "))
        except (TypeError, ValueError):
            print("Altura tem que ser número")
            break
        else:
            listacad.append(Pessoa(nomee, idadee, alturaa))
    else:
        print("Finalizando")
        break

for c in listacad:
    print(c.__dict__)