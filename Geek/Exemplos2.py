'''produto2 = {}

while True:
    item = str(input('nome do item :'))
    quant = int(input('Quantidade :'))
    valor = float(input('Valor da unidade :'))

    op = ' '

    while not op in 'SN':
        op =str(input('Foi Vendida alguma unidade ? [S/N]'))
    if op == 'S':
        vend=int(input('Quantas ? :'))
        quant = quant - vend
        print(quant)
    op2= ' '
    while not op2 in 'SN':
        op2 = str(input('Quer adiconar mais unidades ? [S/ N]'))
    if op2 == 'S':
       print()
    if op2 == 'N':
        break
produto1 = {'item':item, 'Quant': quant,'valor': valor}
print(produto1)'''

'''lista = [1, 2, 3, 4, 5, 6]
lista[1] = 0
print(lista)'''

vetor = []
cont  = 0
for c in range(5):
    n1 = vetor.append((int(input('Digite número:'))))
print(f'Quantidade de numero ')
for indice, n in enumerate(vetor):
    if n % 2 == 0:
        cont += 1

        print(f'{indice}...',end='')
print()
print(f" Quantidade de números pares é {cont} ")



