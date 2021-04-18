sexo=str(input('informe seu sexo :'))
while sexo not in 'mMfF':
    sexo=str(input('Opção Invalida. Digite novamente :'))
print('Sexo {},confirmado'.format(sexo))
