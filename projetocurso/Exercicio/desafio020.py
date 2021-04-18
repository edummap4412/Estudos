from random import shuffle
a=input('Digite nome do primeiro aluno :')
b=input('Digite nome do segundo aluno :')
c=input('Digite nome do terceiro aluno :')
d=input('Digite nome do quarto aluno :')
lista=[a,b,c,d]
print('A ordem de apresentação dos alunos é {}'.format(shuffle(lista)))
print(lista)
