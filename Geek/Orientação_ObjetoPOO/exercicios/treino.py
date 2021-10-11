
def mostra_nome(**kwargs):
    return kwargs['nome'] + kwargs['sobrenome']


nome_completo = mostra_nome(nome='Eduardo',
                            sobrenome='Mascarenhas')
print(nome_completo)
