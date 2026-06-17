n = input('Введите число')

ok = True

for i in range(1, len(n)):
    if n[i] <= n[i - 1]:
        ok = False
        break

print("Да" if ok else "Нет")