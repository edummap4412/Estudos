from math import ceil
sal=int(input('Digite sálario do funcionario :'))
n1=sal*1.10
if sal>=1225.00:
    print('Quem ganhava {} agora o valor do aumento é {}'.format(sal,ceil(n1)))
else:
    print('Quem ganhava {} agora o valor do aumento é {}'.format(sal,ceil(sal*1.15)))

