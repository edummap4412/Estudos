
expr = str(input('Digite Número:'))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb ==' )':
        if len(pilha) > 0: # << le o ultimo elemento ... e verifica se a pilha nao esta vazia
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressao matematica ,Certa')
else:
    print('Expressao matematica ,Errada')
