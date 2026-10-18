a = float(input("a = "))
b = float(input("b = "))
h = float(input("шаг = "))
e = float(input("точность = "))
print("x\t y\t членов")
x = a
while x <= b:
    s = 0
    n = 0
    t = 1
    while abs(t) >= e:
        t = 2 / ((2 * n + 1) * x ** (2 * n + 1))
        s += t
        n += 1
    print(x, "\t", s, "\t", n)
    x += h