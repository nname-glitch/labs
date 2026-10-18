x = float(input("Введите x: "))
y = float(input("Введите y: "))
R = float(input("Введите R: "))

if x**2 + y**2 <= R**2 and ((x >= 0 and y >= 0 and y >= x) or (x <= 0 and y <= 0 and y <= x)):
    print("Попадает")
else:
    print("Не попадает")
