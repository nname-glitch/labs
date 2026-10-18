import math
x = float(input("Введите x: "))
if -3 <= x <= -2:
  y = -x - 2
elif -2 < x < -1:
  y = math.sqrt(1 - (x + 1)**2)
elif -1 <= x <= 1:
  y = 1
elif 1 < x < 2:
  y = -2 * x + 3
elif 2 <= x <= 5:
  y = -1
else:
  y = "не задано"
print("y =", y)
