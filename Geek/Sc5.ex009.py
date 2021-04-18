
while True:
    n = float(input('Sua altura em Metros:'))

    n1 = ' '
    while not n1 in 'MF':
        n1 = str(input('Qual seu sexo ? [M/F]')).strip().upper()

    if n1 == 'M':
        ideal = (72.7*n)-58
        print(f'Seu peso ideal é {ideal}')

