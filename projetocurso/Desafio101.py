

def voto (n):
    from datetime import date
    ano = date.today().year
    s = ano - n
    if s < 16:

        print(f'Nessa idade o voto  não é permitido')
        return s
    elif 16 >= s <18 or s >65:
        print(f'Nessa idade o voto é Opcional')
        return s
    else:
        print(f'Voto é obrigatório. VOTE COM CONSCIÊNCIA')
        return s


nasc = int(input('Qual ano de nascimento?'))
voto(nasc)
