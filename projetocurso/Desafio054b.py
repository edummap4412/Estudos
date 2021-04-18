frase=str(input('Digite uma frase :')).strip().upper()
sep=frase.split()
junto=''.join(sep)
inverso=junto[::-1]
print(junto)
print(inverso)
if junto == inverso :
    print('Tem um Palindromo')
else:
    print('Não há Palindromo')

