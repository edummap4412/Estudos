
Tabela=('Internacional','São Paulo','Flamengo','Atlético-MG',
        'Palmeiras','Grêmio','Fluminense','Ceará Sc','Santos',
        'Corithians','Bragantino','Athletico-PR','Atlético-GO',
        'Sport Recife','Vasco da Gama','Fortaleza','Bahia','Goiás',
        'Coritiba','Botafogo')
print(Tabela)
colocado=Tabela.index('Santos')
for time in Tabela:
    print(f' Os 5 primeiros colocados são {Tabela[:5]}')
    break
print(f'Os 4 ultimos colocados são {Tabela[16:]}')
print(f'Santos está na {colocado}º colocação')
