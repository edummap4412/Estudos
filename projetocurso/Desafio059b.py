n=int(input('Primeiro valor :'))
n1=int(input('Segundo valor :'))
op=0
maior=0
menor=0
while op != 5:
    print('''
        [1]Somar
        [2]Multiplicar
        [3]maior é menor
        [4]Novos números
        [5]Sair do Programa''')
    op=int(input('Qual sua opção?'))
    if op == 1:
        print(f'A soma de {n} + {n1} ={n+n1}')
    elif op == 2:
        print(f'A multiplicação de {n} x {n1} ={n*n1}')
    elif op == 3:
        if n > n1:
            print(f'O {n} é maior que {n1}')
        if n==n1:
            print('São iguais')
        else:
            print (f'{n1}é maior que {n}')

    elif op == 4:
        n=int(input('Digite primeiro valor:'))
        n1=int(input('Digite Segundo valor'))
    elif op == 5:
        break
    else:
        print('Opção Invalida')

