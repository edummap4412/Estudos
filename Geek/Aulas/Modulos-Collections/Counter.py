"""
Módulo Collections - Counter

Collections -> High-performance Container DataTypes

Counter -> Recebe um iteravel como parametro e cria um ojeto do tipo Colletions Counter que é parecido com um dicionario ,
contendo como chave o elemento da lista passada como parametro e como valor a quantidade
de  ocorrencias desse elemento.
"""
# Utilizando  o Counter

from collections import Counter
# Criar um chave e colocou como valor a quantidade de ocorrencias
lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 49, 65, 80]

res = Counter(lista)

print(type(res))

print(res)

# pode ser usada em qualquer iteravel

liesta = Counter('Geek University')
print(liesta)

#Exemplo 3

texto = '''Durante a nossa trajetória de vida,
 passamos por momentos desafiadores que colocam em xeque a nossa motivação
  e a nossa força de vontade, o que afeta diretamente na nossa persistência.
   Sim, alcançar aquilo que desejamos, que idealizamos, nem sempre é fácil,
    é preciso muito esforço e foco e muitas vezes nos deparamos com o fracasso, 
    mas isso não quer dizer que devemos desistir'''

res= Counter(texto)

# Função most.commum é uma funão que mostra as maiores incidencias , ele ira mostrar as 5 maiores insidencias
print(res.most_common(5))
