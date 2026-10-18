import math
a = float(input("Введите a: "))
z1 = 2 * (math.sin(3 * math.pi - 2 * a))**2 * (math.cos(5 * math.pi + 2 * a))**2
z2 = 1/4 - 1/4 * math.sin(5/2 * math.pi - 8 * a)
print("z1 =", z1)
print("z2 =", z2)
