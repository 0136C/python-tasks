osn1 = int(input('Введите длину первого основания'))
osn2 = int(input('Введите длину второго основания'))
vis = int(input('Введите длину высоты'))
if (osn1 > 0 and osn2 > 0 and vis > 0):
    per = osn1 + osn2 + 2 * (vis**2 + ((osn1 - osn2)/2)**2)**0.5
    print(f'Периметр трапеции: {per}')
else:
    print('Значенияи должны быть положительными')
