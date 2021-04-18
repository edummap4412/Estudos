from time import sleep
n=int(input('Digite um número :'))
print('{:=^20} \n do {:=^10}'.format('TABUADA',n))
for c in range(0,11):
    m=c*n
    sleep(0.5)
    print(' {} x {:2} = {}'.format(c,n,m))




