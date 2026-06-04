a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = []
i = j = 0

while i < len(a) or j < len(b):
    val = None
    if i < len(a) and (j == len(b) or a[i] < b[j]):
        val = a[i]
        i += 1
    elif j < len(b) and (i == len(a) or b[j] < a[i]):
        val = b[j]
        j += 1
    else:
        val = a[i]
        i += 1
        j += 1
        
    if not res or res[-1] != val:
        res.append(val)
        
print(res)