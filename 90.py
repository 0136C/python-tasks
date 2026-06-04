N = int(input())
a = list(map(int, input().split()))
res = []

for i in range(N):
    dist = 0
    for j in range(i + 1, N):
        if a[i] == a[j]:
            dist = j - i
            break
    res.append(dist)
    
print(res)