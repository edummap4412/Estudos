import random
'''andamento = [],posicao = []'''
relatorio = {}
n_casas = 0
numero_casas = []
armazena = []

jogadores = ['jogador1', 'jogador2','jogador3', 'jogador4']
# jogadores = [
#     {"nome": 'jogador1', "saldo": 0, "posicao": 0}
#     , 'jogador2','jogador3', 'jogador4'
# ]
#
#
# propriedades =[
#     {"nome":"prop1", "valor": 40, "aluguel": 4, "owner": None},
#     {"nome":"prop2", "valor": 40, "aluguel": 4},
#     {"nome":"prop3", "valor": 40, "aluguel": 4},
# ]

Tabuleiro = {"prop1": 40, "prop2": 40, "prop3": 50, "prop4": 70, "prop5": 30, "prop6": 40, "prop7": 80, "prop8": 90,
             "prop9": 35, "prop10": 60,
             "prop11": 45, "prop12": 25, "prop13": 20, "prop14": 30, "prop15": 15, "prop16": 10, "prop17": 20,
             "prop18": 35, "prop19": 55, "prop20": 30}

for rodada in range(2):
    print(f'{rodada+1}° rodada')
    for j in jogadores:

        relatorio['nome'] = j
        relatorio['pontos'] = 300
        jogar = ' '
        while jogar not in "J":
            print(f'{j} sua vez de jogar o dado')
            jogar = str(input("Aperte J para jogar o dado"))
            if jogar in "J":
                dado = random.randint(1, 6)
                for i in enumerate(Tabuleiro):

        print(relatorio)


