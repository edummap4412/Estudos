"""
POO - CLASSES

Em POO , Classes nada mais são que modelos dos objetos do mundo real sendo representados computacionalmente

Imagine que você queira fazer um sistema para automatizar o controle das lampadas da sua casa.

Classes podem conter:
    Atributos -> Representam as caracteristicas do objeto . Ou seja, pelos atributos conseguimos
    representar computacionalmente os estados de um objeto. No caso da Lampada , possivelmente iriamos querer saber se
    a lampada é 110 ou 220 volts. se ela é branca , amarela , vermelha ou outra cor , qual é a luminosidade dela e etc...

    -Métodos(Funções) -> representam os comportamentos do objeto . Ou seja, as ações que o objeto pode realizar no seu sistema.
    No caso de lâmpada por exemplo um comportamento comum que muito provavelmente iriamos querer represenjtar no nosso
    sistema é o de liga e desligar


Em python para definir uma classe utilizamos a palavra reserada class

OBS: Ultimilizamos a palavra 'pass em python quando temos um bloco de codigo que ainda não esta implementado

OBS: Quando nomeamos nossas classes em Python utilizamos por conveção o nome do inicial
em maiusculo. Se o nome for composto. Utiliza-se as iniciais de ambas as alavras em maiúsculo, todas juntas.

OBS: Quando estamos planejando um sofware e definimos quais classses teremos que ter no sistema, chamamos
estes objetos que serão mapeados para classes de entidade
"""
idade = 32

preco = 2333.50

nome = 'Eu amo programação'

print(type(idade))
print(type(preco))
print(type(nome))

class Lampada:
    pass

lamp = Lampada

print(type(lamp))
