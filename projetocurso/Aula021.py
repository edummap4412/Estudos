def fatorial(num):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(6)
f3 = fatorial(5)
print(f1, f2, f3)

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input("Digite numero >"))
if par(num):
    print('É par')
else:
    print('É impar')
