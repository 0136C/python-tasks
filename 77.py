N = int(input())
a = list(map(int, input().split()))

best = 0
cur = 0

for x in a:
    if x % 2 == 0:
        cur += 1
        best = max(best, cur)
    else:
        cur = 0

print(best)