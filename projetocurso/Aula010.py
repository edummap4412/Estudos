'''nome=str(input('Digite seu nome :')).strip()
if nome =='Eduardo':
    print('Continue se esforçando')
else:
    print('Belo nome')
print('Bom dia para você, {}'.format(nome)'''

n1=float(input('Digite sua nota na primeira avaliação :'))
n2=float(input('Digite sua nota na segunta avaliação :'))
media=(n1+n2)/2
print('Nota da primeira av: {}\n Nota da segunda Av: {}\n Media {}'.format(n1,n2,media))
if media<=4.9:
    print('Aluno Reprovado')
else:
    print('Aluno Aprovado')










