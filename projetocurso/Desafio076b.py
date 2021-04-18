lista=('Eduardo', 26, 'Juca', 30, 'Josias', 20, 'Benedito', 20, 'Karina', 40, 'Flavia', 19)
print('-'*46)
print(f'{"Lista De Convidados":^45}')
print('-'*46)
for c in range(0, len(lista)):

    if c % 2 == 0:
        print(f'{lista[c]:<30}', end=' ')
    else:
        print(f'{lista[c]:>10} anos')

