y = float(input("Градусы: "))

# 360 градусов = 720 минут. Значит 1 градус = 2 минуты.
total_minutes = int(y * 2)
hours = total_minutes // 60
minutes = total_minutes % 60

print("Часов:", hours, "Минут:", minutes)