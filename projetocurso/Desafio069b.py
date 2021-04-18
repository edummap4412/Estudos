sexo=''
op=' '
idade=int(input('Idade:'))
while op != 'N':
    while sexo != 'M' and sexo != 'F':
        sexo=str(input('Qual seu sexo ? [M/F]')).strip().upper()

    op=str(input('Quer continuar? [S/N]')).strip().upper()

    if op == 'S':
        idade=int(input('Idade :'))
        sexo=str(input('Qual seu sexo? [M/F]'))
        
