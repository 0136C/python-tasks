a = list(map(int, input().split()))

if a == a[::-1]:
    print("Список ялвяется палиндромом")
else:
    print("Список не ялвяется палиндромом")