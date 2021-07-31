import random
dado = random.randint(1, 6)
pontos = {}
sorteio = []
rodada = 10

Tabuleiro = {"prop1": 40, "prop2": 40, "prop3": 50, "prop4": 70, "prop5": 30, "prop6": 40, "prop7": 80, "prop8": 90,
             "prop9": 35, "prop10": 60,
             "prop11": 45, "prop12": 25, "prop13": 20, "prop14": 30, "prop15": 15, "prop16": 10, "prop17": 20,
             "prop18": 35, "prop19": 55, "prop20": 30}


def sorteia(a):

    random.shuffle(jogadores)
    print(jogadores)

jogadores = ['jogador1', 'jogador2', 'jogador3', 'jogador4']

sorteia(jogadores)
