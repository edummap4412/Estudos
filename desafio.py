

def universo(n1=3, n2=5):
    """
     Função que indica quando o número é multiplo de x e y ele mostra "Universo"
     se não se for multiplo somente de x mostra "UNI" e de y mostra "VERSO"
    """
    a = n1
    b = n2
    for n in range(1, 101):
        if n % a == 0 and n % b == 0: # condição para validar se o número é multiplo de ambos
           print(f'{n} UNIVERSO')
        else:
            if n % a == 0:
                print(f'{n} UNI')

            if n % b == 0:
                print(f'{n} VERSO')

num = universo()




