N = int(input())
a = list(map(int, input().split()))

for i in range(1, N):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        print(a[i])
        break
else:
    print("no")