N = int(input())
a = list(map(int, input().split()))

last = None

for i in range(1, N - 1):
    if a[i] < a[i - 1] and a[i] < a[i + 1]:
        last = i

if last == None:
    print("no")
else:
    print(last)