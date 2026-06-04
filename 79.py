N = int(input())
a = list(map(int, input().split()))

s = 0
found = False

for x in a:
    if x == s:
        found = True
        break
    s += x

if found:
    print('Да')
else:
    print("Нет")