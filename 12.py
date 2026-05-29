# 20 квартир на 5 этажей = 4 квартиры на этаж
kv = int(input("Номер квартиры (от 1 до 20): "))

floor = (kv - 1) // 4 + 1
position = (kv - 1) % 4 + 1

print("Этаж:", floor)
print("По счету на этаже:", position)