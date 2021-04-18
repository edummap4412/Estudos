
nota=float(input('Avaliação 1 :'))
nota2=float(input('Avaliação 2 :'))
media=(nota+nota2)/2
print('Sua média é {:.2f}'.format(media))

if media >7 :
    print('Aluno Aprovado')
elif  media >4 or media == 6.9:
    print ( 'Aluno de Recuperação')
else:
    print('Aluno reprovado')







