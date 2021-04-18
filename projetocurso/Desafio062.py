
primeiro=int(input('Digite o primeiro termo:'))
razão=int(input('Digite a Razão :'))
s=primeiro
cont=1
mais=10
total=0
while mais !=0:
    total+=mais
    while cont <= total:
        print(f'{s}',end=' ')
        s+=razão
        cont+=1
    print('PAUSE')
    mais=int(input('Quantos termos você quer mostrar a mais ?'))
print('Fim')
