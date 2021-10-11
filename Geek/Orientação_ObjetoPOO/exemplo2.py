while True:
    n =int(input('Digite um Número:'))
    if n == 0:
        break
    if n % 2 == 0 :
        print('Número Par')
    try:
        m =int(input('Quer multiplcar o numero?'))
