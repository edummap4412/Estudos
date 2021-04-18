num=int(input('Digite um número :'))
dig=str(input('''Para Qual unidade deseja converter 
[ 1 ] Binario
[ 2 ] Octal
[ 3 ] Hexadecimal''')).strip()
op=int(input('Escolha Opcão :'))
if op == 1:
    print('Numero {} em binario fica {}'.format(num,bin(num)[2:]))
elif op == 2:
    print('Número {} em Octadecimal fica {}'.format(num,oct(num)[2:]))
elif  op == 3:
    print('Número {} em Hexadecimal fica {}'.format(num,hex(num)[2:]))
else:
    print(' Opção invalida')














