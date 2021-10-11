lista1= ([ 'apple', 'banana', 'blueberry', 'banana', 'blueberry', 'coconut', 'blueberry', 'coconut', 'lemon',  'mango'])

lista2 = (['melon', 'banana', 'pineapple', 'banana', 'melon', 'coconut', 'watermelon', 'coconut',  'watermelon', 'orange'])

lista3 = []

for l in lista1:
    for l2 in lista2:
        if l == l2:

            lista3.append(l)

print (lista3)

