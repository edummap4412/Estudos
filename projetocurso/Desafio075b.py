num=(int(input('Digite um número:')),
     int(input('Digite um número:')),
     int(input('Digite um número:')),
     int(input('Digite um número:')))
print(f'O número que você digitou {num}')
if 3 in num:
    print(f'número 3 está na posição {num.index(num)}')
else:
    print(f'Não há número 3 ')

print(f'O número 9 aparece {num.count(9)}')
print(f'Os números pares digitados são :',end=' ')
for c in num:
    if c % 2==0:
        print(c,end=' ')

