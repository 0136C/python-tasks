n = input('Введите число')

best = 1
cur = 1

for i in range(1, len(n)):
    if n[i] == n[i - 1]:
        cur += 1
        best = max(best, cur)
    else:
        cur = 1

print(best)