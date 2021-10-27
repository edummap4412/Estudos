def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta


def deposita(conta, valor):
    conta["saldo"] += valor


def sacar (conta , valor):
    conta["saldo"] -= valor


def extrato (conta):
    print(f' Seu saldo em conta é {conta["saldo"]}')
      