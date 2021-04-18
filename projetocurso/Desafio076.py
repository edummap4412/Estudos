produtos=('batata',2 ,'ovo',5,'Macarrão',8,'Carne',9,'Feijão',10)

print('-'*43)
print(f'{"Mercado Programe MAIS":^40}')
print('-'*43)

for n in range(0, len(produtos)):
    if n % 2 == 0:
        print(f'{produtos[n]:.<30}',end=' ')
    else:
        print(f'R${produtos[n]:>3}')





