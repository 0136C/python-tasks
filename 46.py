n = int(input("Введите число"))

for digit in range(10):
    count = 0
    temp = n

    if temp == 0 and digit == 0:
        count = 1

    while temp > 0:
        if temp % 10 == digit:
            count += 1
        temp //= 10

    print("число", digit, "-", count, "раз")