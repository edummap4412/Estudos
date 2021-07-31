'''for c in range(101):
    print(c)
while c != 100:
    c += 1
    print(c)'''
cont = 0

s = 0
while True:
    for c in range(101):
        print(c)
        if c == 100:
            cont += 1
    if cont >= 3:
        break
