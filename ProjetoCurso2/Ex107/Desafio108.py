from Ex107 import moeda

p = int(input('Valor:'))

print(f'O dobro de {moeda.mostra(p)} é {(moeda.dobro(p))}')
print(f'A metade de {moeda.mostra(p)} é {(moeda.metade(p))}')
print(f"Aumentar 10%, temos {(moeda.aumento(p))}")
