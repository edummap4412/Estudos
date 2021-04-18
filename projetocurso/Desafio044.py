print('{:=^40}'.format('Lojas Eduletronicos'))

prod=int(input('Qual valor do produto R$'))
print('Escolha a forma de pagamento :  [ 1 ] Dinheiro [ 2 ] Cartão ')
op=int(input('Selecione Opção :'))
if op == 2:
    prest=int(input('Em quantas parcelas :'))
    if prest == 1:
        print('Valor de R${} em 1x ,parcela recebe %5 de desconto ficando R${}'.format(prod,prod*0.95))
    elif prest == 2 :
        print('Valor de R${}  em 2x fica {}reais'.format(prod,prod/2))
    elif prest >=3:
        print('Valor de R${} em 3x(ou mais)recebe juros 20% ficando R${} \nValor da parcela R${} em {}x'.format(prod,prod*1.20,prod*1.20/prest,prest))
elif op ==1:
    print('Valor de R${} no dinheiro/cheque tem 10% de desconto ficando R${}'.format(prod,prod*0.90))







