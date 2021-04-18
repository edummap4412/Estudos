cont=0
n=int(input('Digite um número :'))
for c in range(1,n+1):
    if n % c == 0 :
        cont+=1
if cont == 2 :
    print('{} é Número PRIMO'.format(n))
else:
    print('{} não é número PRIMO'.format(n))


# Todo numero primo deve ser dividido por 1 e por ele mesmo , para ser.