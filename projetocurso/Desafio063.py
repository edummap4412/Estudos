n=int(input('Digite Termos :'))
t1=0
t2=1
cont=3
mais=0
print('{} {}'.format(t1,t2),end=' ')
while mais!=0:
    cont=3

    while cont <= n:
        t3=t2+t1
        print('{}'.format(t3),end=' ')
        t1=t2
        t2=t3
        cont+=1

#cont = 3 signiica que o contador vai passar a conta apartir do 3.
