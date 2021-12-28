
estados = [
    (1, 'São Paulo'),
    (2, 'Minas Gerais'),
    (3, 'Mato Grosso'),
    (4, 'Espeirito Santo'),
    (5, 'Rio Grande do Sul'),
    (6, 'Pará'),
    (7, 'Paraná'),
    (8, 'Sergipe'),
    (9, 'Bahia'),
]

brasil = {ddd: estado for ddd, estado in estados if 'Ceará'}


if not brasil:
    print('São Paulo no Brasil')
print('Tem Ceará')

