a = list(map(int, input().split()))

max_index = 0

for i in range(1, len(a)):
    if a[i] > a[max_index]:
        max_index = i

print(max_index)