lista = ('Calça', 'Ameixa', 'Mamão', 'Tênis', 'Sofá', 'Paralelepipedo')
for n in lista :
    print(f'\nPara palavra {n} temos:')
    for letra in n :
        if letra.lower() in 'aeiou':
            print(f'{letra}',end=' ')
