N = int(input())
a = list(map(int, input().split()))

best = a[0]
best_count = a.count(a[0])

for x in a:
    if a.count(x) > best_count:
        best = x
        best_count = a.count(x)

print(best, best_count)