num=int(input('Digite um numero :'))
n= num//1 % 10
n1=num//10 % 10
n2=num//100 % 10
n3=num//1000 % 10
print('Unidade: {}\n Dezena: {}\n Centena: {}\n Milhar: {}'.format(n,n1,n2,n3))

