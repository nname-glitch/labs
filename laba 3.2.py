import random
R = float(input("Введите радиус R: "))
for i in range(10):
  x = random.uniform(-R, R)
  y = random.uniform(-R, R)
  if (x * x + y * y <= R * R and x <= 0 and y >= 0) or \
    (y <= -2 * x and y >= 2 * x - 2 * R):
    print("Выстрел", i + 1, "попал")
  else:
    print("Выстрел", i + 1, "не попал")
  print("Координаты:", x, y)
