lanche= 'Suco','Hamburguer','Pizza','Pudim'
'''print(lanche)
for c in lanche[1:]:
    print(f'Eu vou comer {c} e beber {lanche[0]}')'''
#for cont in range(0,(len(lanche))):
#    print(lanche[cont])

#for pos, c in enumerate(lanche):
#    print(sorted(f'Vou comer {c} na posição {pos}'))

#Comando 'sorted para colocar elas em ordem alfabetica, só altera a forma que sao mostradas pois Tuplas sao imutaveis
# TUPLAS SAO IMUTAVEIS

'''a=(5,6,4,5)
b=(4,5,6,9)
c=a+b
print(len(c))
print(c.count(4))
print(c.index(2))'''
# Somando as tuplas nao soma o numero porem aparecem juntas
# com len ele conta a quantidade de tuplas
# cont para conta numeros de vezes que 4 aparrece
#  index para identificar identifica posição
a=(5,6,4,5)
del(a)
b=(4,5,6,9)
c=a+b
print(c)
print(c.index(5,4))
# esse virgula (5 '',4'') indica qual possicao esta o numero , chamado de deslocamento

