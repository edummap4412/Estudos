valor = int(input('Digite valor a ser sacado : R$'))
total = valor
ced = 100
totced=0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f' Total de {totced} celulas de R$ {ced}')
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        elif ced == 2:
            ced = 0
        totced = 0
        if totced == 0:
            break



