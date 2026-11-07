import turtle
import math
import random

#Настройки экрана
screen = turtle.Screen()
screen.title("Задание 2: Метод Монте-Карло")
screen.setup(width=0.8, height=0.8)
screen.bgcolor("#ffffff")

#Отключаем трассировку для мгновенного вывода 10000 точек
screen.tracer(0, 0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
R = 4.0
N = 10000  # Количество испытаний по заданию
scale = min(screen.window_width(), screen.window_height()) // (R * 2.5)

#Рисуем оси
t.color("#bdc3c7")
t.goto(0, -int(R+1)*scale); t.pendown(); t.goto(0, int(R+1)*scale); t.penup()
t.goto(-int(R+1)*scale, 0); t.pendown(); t.goto(int(R+1)*scale, 0); t.penup()

#Градация осей
t.color("#7f8c8d")
for val in [-int(R), int(R)]:
    t.goto(val * scale, -5); t.pendown(); t.goto(val * scale, 5); t.penup()
    t.goto(val * scale, -20); t.write(f"{val}(R)", align="center", font=("Arial", 9))

hits = 0
#Область генерации точек
x_min, x_max = -R, R
y_min, y_max = -R, R
S_rect = (x_max - x_min) * (y_max - y_min)

#Моделирование выстрелов
for _ in range(N):
    x = random.uniform(x_min, x_max)
    y = random.uniform(y_min, y_max)
    
    #Условие попадания в заштрихованную область
    is_hit = (x * x + y * y <= R * R and x <= 0 and y >= 0) or \
             (y <= -2 * x and y >= 2 * x - 2 * R)
             
    t.penup()
    t.goto(x * scale, y * scale)
    if is_hit:
        hits += 1
        t.dot(3, "#2ecc71")  #попал
    else:
        t.dot(2, "#dfe6e9")  #мимо

#Расчет площадей
S_calc = (hits / N) * S_rect
#геометрическая площадь: 1/4 круга + площадь нижнего треугольника
S_real = (math.pi * (R**2)) / 4 + (R**2) / 2
error_pct = abs(S_calc - S_real) / S_real * 100

#Вывод результата
t.penup()
t.goto(-screen.window_width() // 2 + 40, -screen.window_height() // 2 + 40)
t.color("#2c3e50")
t.write(f"Реальная площадь: {S_real:.4f}\n"
        f"Монте-Карло площадь: {S_calc:.4f}\n"
        f"Погрешность: {error_pct:.2f}%", 
        font=("Arial", 11, "bold"))

screen.update()
screen.mainloop()