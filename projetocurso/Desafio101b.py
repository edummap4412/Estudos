
def voto (ano):
    from datetime import date
    a = date.today().year
    idade = a - ano
    if idade < 16:
        print(f'Sua idade é {idade} anos: VOTO NÃO PERMITIDO')
        return idade
    if 16 >= idade < 18:
        print(f'Seu aidade é {idade} anos:VOTO OPCIONAL')
        return idade
    else:
        print(f'Sua idade é {idade} anos: VOTO OBRIGATÓRIO')


nasc = int(input('Qual foi seu ano de você nascimento ?'))
voto(nasc)