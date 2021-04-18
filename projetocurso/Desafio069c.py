while True:
    idade=int(input('Digite sua idade:'))
    sexo=' '
    while not sexo in 'MF':
        sexo=str(input('Sexo: [M/F]')).strip().upper()
    op=' '

    while not op in 'SN':
        op=str(input('Quer continuar? [S/N]')).strip().upper()
    if op == 'N':
        break
# Estrutura de Looping que repete pergunta até colocar  Letra correta
