from moeda import dobro, aumento, diminuir

n = int(input('Valor R$ :'))
print(f'O dobro do valor é R${dobro(n)}')
print(f'O aumentando em 10% R${aumento(n):.2f}')
print(f'O diminuindo em 13% R${diminuir(n):.2f}')
