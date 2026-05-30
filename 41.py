n = int(input("Введите число: "))

maxi = 0
while n > 0:
    ch = n % 10

    if ch > maxi:
        maxi = ch

    n = n // 10
print(maxi)