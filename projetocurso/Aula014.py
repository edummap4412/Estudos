n = 1
soma = 0
cont = 0
maior = 0
menor = 0
par=impar=0
while n != 0:
    n = int(input('Digite um número :'))
    soma += n

    if n != 0:
        cont+=1
        menor=n
        maior=n
        if maior > n:
            maior = n

        if menor > n:
            menor=n
    if n!= 0:
       if n % 2 ==0:
           par+=1
       else:
           impar+=1




print('Maior é {}'.format(maior))
print('Menor é {}'.format(menor))
print('Quantidade de numeros pares é {} \nQuantidade de numeros impares é {}'.format(par,impar))
print('Quantidade de numeros digitados é {}'.format(cont))


