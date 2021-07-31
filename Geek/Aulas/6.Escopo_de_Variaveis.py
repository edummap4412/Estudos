'''
Escopo de variaveis
/                        / < esse espaço é um escopo

Dois casos de escopo:

1-Variavies globais: são reconhecidas ou seja seu escopo compreende todo o programa

2- Varias locais : são reconhecidas apenas no bloco onde foram declaradas , ou seja, seu escopo está limitado ao bloco
onde foi declarado

Para declarar variavies em pyhton fazemos:

nome_da_variavel = valor_da_variavel
Exemplo em C:
int numero = 42
Exemplo em Java :
int numero = 42

Python nao precisa pois ele ja sabe que o type da variavel é inteiro

'''

numero = 42 # Variavel Global

if numero >10 :
    novo=numero + 10 # Variavel Local só funciona aqui, para transformar em global jogamos  no top
    print(novo)
