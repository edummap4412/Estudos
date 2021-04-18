n=0
n2=0
maior=0
menor=0
nome=' '
for c in range (1,3):
    n1=str(input('Digite seu nome ')).strip().upper()
    n=int(input('Digite um peso :'))
    n2=float(input('Digite sua Altura:'))
    if c ==1 :
        maior=n
        menor=n
        nome=n1
    else:
        if maior < n:
            maior = n
            nome=n1
        if menor > n:
            menor = n

print('Maior peso é {}, seu nome é {},seu IMC é {:.2f}'.format(maior,nome,n*(n2/n2)))
print('Menor peso é {}'.format(menor))





