while True :
    n=int(input('Número:'))
    if n <0 :
        break
    for c in range(0,11):
        print(f'{c}x{n}={c*n}')
# Sempre lembrar da posicão correta do break , é um verificação para continuar ou parar o programa
