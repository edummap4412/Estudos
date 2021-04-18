valor=int(input('Que valor você quer sacar? R$'))
total=valor
ced=50
totced=0
while True:
    if total >=ced:
        total-=ced
        totced+=1
    else:
        if totced>0:
            print(f'total de no')
