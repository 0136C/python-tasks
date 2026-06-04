a = list(map(int, input().split()))

best = a[0]

for x in a:
    if a.count(x) > a.count(best):
        best = x

print(best)