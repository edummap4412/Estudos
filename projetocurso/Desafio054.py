'''frase=str(input('Digite uma Frase :')).strip().upper()
separado=frase.split()
junto=''.join(separado)
inverso=''
for c in range(len(junto)-1,-1,-1):
    inverso+=junto[c]
print(inverso)
if inverso == junto:
    print('Temos um Palindromo')
else:
    print('Nao é Palindromo')'''

frase=str(input('Digite uma frase:')).strip().upper()



