from time import sleep
def contador(i, f, p):

    if p < 0:
        p *= -1
    if p == 0:

        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            cont += p
            print(cont, end=' ',flush=True)

        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)# usar flush em versoes mais atualizadas do Pycharm

            cont -= p
        print('FIM')
contador(0,10,1)
contador(10, 0, 1)

print('Agora é sua vez de personalizar a contagem')
ini =int(input('Inicio:'))
fim = int(input('Fim:'))
pas = int(input('Passo:'))
