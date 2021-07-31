'''palavras=(str(input('NOME :')))
for indice, letra in enumerate(palavras):'''
'''
'Loop -> Estrutura de Repetição'
'For -> Uma dessas Estruturas'
Utilizamos loops para itrar sobre sequencias ou sobre Valores iteravéis:
-String
 nome = 'Geek University'
-Lista
 lista = [1, 2, 3, 4, 5, 6]
-Range 
numeros = range(1,10)

'''
'''nome = 'Geek University'
lista = [1, 3, 5, 7, 9]

# Exemplo de for 1
for letra in nome:
    print(letra)
#Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)
#Exemplo de  for  3 (Iterando sobre um range)
for numero in range(1, 10):
    print(numero)'''

''''
Enumerate

(C ,0) ,(o,1) ,(n,2), (t,3).....
'''
nome = 'Continua a Nadar'
'''for indice, n in enumerate(nome):
    print(nome[indice]'''
''' se no lugar do 'indice' usar '_' voce descarta o valor .'''
for valor in enumerate(nome):
    print(valor[1],end='')

'''Complementos para String'''
'''EMOJI
'''
#Original: U+1F60D
#Modificado(para Python): U0001F60D
'''Tabela de Emojis Unicode : https://apps.timwhitlock.info/emoji/tables/unicode

'Concatenação de String'

nome = 'Continue'
emoji = 'U0001F60D'

for num in range(1,11):
    print('\U0001F60D'*num)




