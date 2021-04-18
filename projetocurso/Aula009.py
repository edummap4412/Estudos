'''frase=str(input('Digite um nome :').strip())
frase1=frase.split()
frase2=''.join(frase1)
print(frase1[2][4])
print(len(frase)-frase.count(' '))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(len(frase1[1]))
print(frase2)
print(frase.rfind('a')-frase.count(' '))'''



'''frase='Curso eduardo michael computadores'
frase=frase.replace('computadores','Ar-condicionado')
print(frase)'''


#para a string mudar defitivamente quando usamos o comando 'frase.replace'
#frase=frase.replace( nome , nome que substitui)


# Manipulando texto
#Fatiamento de string
#frase.count('o') para contar vezes que aparece letra 'o' minuscula
frase=str(input('FRASE:'))
frase0=frase.split()
frase1=''.join(frase0)
inverso=''
for c in range(len(frase1)-1,-1,-1):
    inverso+=frase1[c]
print(inverso)
if inverso == frase1:
    print('Você tem um Palindromo')

#frase.count('o',0,13) procura letra entre o caracter 0 a 13
#frase.find('chael') encontra a possição do caracter
#frase.rfind('chael') Encontra a possiçaon do caracter a direita( ultimo caracter)
#Transformação
#'eduardo'in frase = detecta a palavra 'eduardo' e aponta True.
#frase.replace('Eduardo' , 'Oraude) troca o nome escolhido.
#frase.upper()=todas as letras ficam maiuscular
#frase.lower()=fica tudo minusculo
#frase.capitalize()= deixa todos os caracteres minusculos menos a primeira letra
#frase.title()=  coloca todas a primeiras letras mauisculo
#frase.strip() = remove espaços inutil
#frase.rstrip()= remove espaços da direita
#frase.lstrp()= remove espaços da esquerda
#Divisão
#frase.split()= divide a strig onde cada palavra tem sua contagem de espaços separado
#'-',join(frase) = juntar as strings, '-'  nos espaços.

#len(frase) = le o numero de caracteres
# frase[9] ira identificar somente o caracter colocado no [], que é o
# decimo caracter pois a contagem inicia-se do 0
#frase[9:13] significa que vai do 9 ao 12 pois 13 nao conta.
#frase[[9:13:2] vai do 9 ao 12 pulando de 2 em 2
#frase[:9] vai até o 9
#frase[15:] começa do caracter  15
#frase[9::3] começa do 9 pulando 3 em 3