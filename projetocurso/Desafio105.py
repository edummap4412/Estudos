
def notas(*num, sit=True):
    soma = 0
    dados = {}
    maior = 0
    menor = 0
    for ind, valor in enumerate(num):
        soma += valor
        if valor == 0:
            maior = menor = 0
        else:
            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor
    med = (soma / len(num))
    dados['total'] = len(num)
    dados['media'] = med
    dados['maior'] = maior
    dados['menor'] = menor
    if sit :
        if med >= 6.5:
            dados['Situação'] = 'Boa'
        if 5.0 < med <= 6.4:
            dados['Situação'] = 'Recuperação'
        else:
            dados['Situação'] = 'Ruim'
    print(dados)


notas(0 ,6, 5, 4, 6,sit =True)

