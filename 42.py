n = int(input('Введите число;'))

original = n
pal = 0

while n > 0:
    pal = pal * 10 + n % 10
    n //= 10

if original == pal:
    print("Да")
else:
    print("Нет")