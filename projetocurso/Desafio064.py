n=1
s=0
cont=0
while n!= 999:
    n=int(input("Digite um Número:"))

    if n!= 999:
            s+=n
            cont+=1
print('Quantidade de numeros digitados foi {}'.format(cont))
print('Valor da Soma é {}'.format(s))
