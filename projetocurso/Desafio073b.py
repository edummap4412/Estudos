Tabela=(' ','Internacional','São Paulo','Flamengo','Atlético-MG','Palmeiras',
        'Grêmio','Fluminense','Ceará Sc','Santos','Corithians','Bragantino',
        'Athletico-PR','Atlético-GO','Sport Recife','Vasco da Gama','Fortaleza'
        ,'Bahia','Goiás','Coritiba','Botafogo')
colocado=Tabela.index('Santos')
for cont in range(1,len(Tabela)):
    print(Tabela[cont],end=' ')
print('-=-'*40)
print(f'Os 5 primeiros colocados são {Tabela[1:6]}.')
print('-=-'*40)
print(f'Os 4 ultimos colocados são {Tabela[16:20]}.')
print('-=-'*40)
print(f'Santos está na {colocado}º posição do campeonato brasileiro.')
print('-=-'*40)
print(sorted(Tabela[1:]))