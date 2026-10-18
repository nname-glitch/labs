import math
x1 = float(input("Введите начальное значение x: "))
x2 = float(input("Введите конечное значение x: "))
dx = float(input("Введите шаг dx: "))
print("x y")
x = x1
while x <= x2:
 if x <= 0:
   y = -x / 2 - 3
 elif x <= 3:
  y = -math.sqrt(9 - x**2)
 else:
  y = math.sqrt(9 - (x - 6)**2)
 print(x, y)
 x = round(x + dx, 10)
