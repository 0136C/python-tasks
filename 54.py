n = int(input("Введите число"))
a = list(map(int, input().split()))

best = 1
cur = 1

for i in range(1, n):
    if a[i] < a[i - 1]:
        cur += 1
        best = max(best, cur)
    else:
        cur = 1

print(best)