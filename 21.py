a = int(input())
b = int(input())
c = int(input())

s = a + b + c

if a > b and a > c:
    result = b * c
elif b > a and b > c:
    result = a * c
else:
    result = a * b
print(result)