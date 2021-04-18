s=cont=0
while True :
    n=int(input('Digite um Número(999 para parar) :'))
    if n ==999:
        break
    cont+=1
    s+=n
print(f'Foram digitados {cont} e a soma deles é igual a {s}')

