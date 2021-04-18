num = int(input('Digite um número: '))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        cont += 1

if cont > 2:
    print('Esse número não é Primo')
else:
      print('Esse número é Primo')
