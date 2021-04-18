q=float(input('Quandtos Km rodados :'))
d=float(input('Dias de uso :'))
valor=(q*0.15)+(d*60)
print('Veiculo rodou Km{} valor :{} reias  \n foi usado por {} dias {} reais'.format(q,(q*0.15),d,(d*60)))
print('Valor a pagar é R$ {}'.format(valor))


