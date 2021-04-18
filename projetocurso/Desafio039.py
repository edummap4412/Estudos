from datetime import date
sexo=str(input('Qual seu Sexo : Homem ou Mulher ')).strip()
opcao=int(input('Escolha :'))
if opcao == 1:
    print('Comparecimento é Obrigatório')
elif opcao == 2:
    print('Comparecimento é Facultativo')
else:
    print('opçao invalida')

idade=int(input('Digite seu ano de nascimento :'))
ano=date.today().year
sub=ano-idade
sub2=2020-idade
if sub == 17:
    print('Sua idade é {} anos. Compareça a Junta de Militar com RG'.format(sub))
elif sub >=18 :

    print('Você tem {} anos e ja passou do prazo em {} anos.Justifica sua ausencia na Junta Militar '.format(sub2,sub-17))
    ano1= sub-17
    ano2=ano-ano1
    print('Seu alistamento foi em {}'.format(ano2))
elif sub <=16:
    print('Você tem {} anos .Daqui {} anos compareça a Junta Militar'.format(sub,17-sub))
    ano3=17-sub
    ano4=ano3+idade
    print('Você se alistará na junta militar em {}'.format(ano4))

print('Acesse o site www.eduardovocevaiconseguir.com.br para mais informações')




