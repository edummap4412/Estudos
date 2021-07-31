'''
Estruturas Logicas AND, OR, NOT, IS
 Operadores Unarios
 NOT
 'Para o NOT o valor do booleano é invertido,ou seja, se for True vira False.
print(not True)
mostra 'False'
print(not False)
mostra 'True'

 Operadores Binarios

 AND, OR, IS
 IS = é oque está se True é True , se False é False. Valor é comparado com outro
'''
ativo = False
logado = False

if ativo and logado:
    print(f'Seja Bem-vindo.')
else:
    if not logado:
        print('Usuario não logado')
    if not ativo:
        print('Usuario não ativo')
    if not ativo and logado == False:
        print(f'Usuario Desconectado')

# Ativo é Falso?
'''print(ativo is False)
# mostra "False" pois ativo é verdadeiro.
#se ativo for 'False' mostar Verdadeiro

nome='EDUARDO'
print(nome.upper().isupper())'''

