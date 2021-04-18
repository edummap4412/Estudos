emp=float(input('Qual valor que deseja para empréstimo?'))
sal=float(input('Qual valor do seu salário ?'))
pres=float(input('Quantos anos voce deseja pagar esse valor ?'))
sal1=sal*1.30
pres1=emp/(pres*12)
mens=emp/pres

if sal1<pres1 :
    print('Emprestimo não pode ser aprovado .Pois Salario é {} o valor das parcelas {:.2f}'.format(sal,pres1))
else:
    print('Emprestimo aprovado.Seu salario é {} valor da prestação em {:.2f}/ mes'.format(sal,pres1))



