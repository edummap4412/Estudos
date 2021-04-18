op=''
cont=menor=0
s=0
nome=''


produto=str(input('Nome do Produto :')).strip()
valor=int(input('Preço:R$ '))
s+=valor
if menor < valor :
    menor=valor
    nome=produto
    if valor >=1000:
        cont+=1
while op!= 'N':
    op=str(input('Quer continuar ? [S/N]')).strip().upper()

    if op =='S':
        produto=str(input('Produto:')).strip()
        valor=int(input('Preço :R$ '))
        s+=valor

        if menor > valor:
            menor=valor
            nome=produto
        if valor>=1000:
            cont+=1
               
print(f'menor valor {menor:.2f} e é {nome}')
print(f'Quantidade de itens acima de 1000 R$ é {cont}')
print(f'valor total fica {s:.2f}')
# Continuar , Solucoa para menor valor e seu nome







