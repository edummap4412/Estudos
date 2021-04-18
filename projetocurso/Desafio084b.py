temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] > men:
            men = temp[1]
    princ.append(temp.copy())
    temp.copy()
    op = str(input('Quer continuar? [S/N]'))
    if op in 'N':
        break
print(f'Nome das pessoas com maior peso :')
for p in princ:
    if p[1] == mai:
        print(p[0])
print(f'Nome das pessoas com menor peso:')
for p in princ:
    if p[1] == men:
        print(p[0])
