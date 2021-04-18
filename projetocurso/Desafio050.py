s=0
cont=0
s1=0
cont1=0
for c in range(1,8):
    n=int(input('Digite {}º número :'.format(c)))
    if n % 2 == 0 :
        s+=n
        cont+=1
    elif n % 2 == 1:
        s1+=n
        cont1+=1

print('Você digitou {} numeros pares e a soma deles é {}'.format(cont,s))
print('Você digitou {} numeros impares e a soma dele é {}'.format(cont1,s1))
