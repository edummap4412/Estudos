def leiaint(a):
    while True:
        s = (input(a))
        if s.isnumeric():
            return s
        else:
            print('\033[0;31mErro , Digite número inteiro\033[m')


n = leiaint('Digite número:')
print(f'Número digitado foi {n}')
