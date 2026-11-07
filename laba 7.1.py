import turtle
import math

#граф окно
screen = turtle.Screen()
screen.title("Лабораторная работа №7: Программирование графики")
screen.setup(width=800, height=600)
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)  #скорость рисования
t.hideturtle()

#кэфы масштабирования (1 единица графика = 30 пикселей на экране)
SCALE = 30

def draw_axes():
    """Функция для отрисовки осей координат и разметки"""
    t.pencolor("gray")
    t.pensize(1)
    
    # Рисуем ось X
    t.penup()
    t.goto(-350, 0)
    t.pendown()
    t.goto(350, 0)
    
    # Рисуем ось Y
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.goto(0, 250)
    
    #Подписи к осям
    t.penup()
    t.goto(330, 10)
    t.write("X", font=("Times New Roman", 12, "bold"))
    t.goto(10, 230)
    t.write("Y", font=("Times New Roman", 12, "bold"))
    
    #Нанесение засечек и подписей чисел (от -10 до 10)
    for i in range(-10, 11):
        if i == 0:
            continue
        # засечки по x  
        t.penup()
        t.goto(i * SCALE, -5)
        t.pendown()
        t.goto(i * SCALE, 5)
        t.penup()
        t.goto(i * SCALE - 5, -20)
        t.write(str(i), font=("Times New Roman", 8, "normal"))
        # засечки по y
        t.penup()
        t.goto(-5, i * SCALE)
        t.pendown()
        t.goto(5, i * SCALE)
        t.penup()
        t.goto(-25, i * SCALE - 5)
        t.write(str(i), font=("Times New Roman", 8, "normal"))

def calculate_y(x):
    """Вычисление значения y по вашей кусочной функции"""
    if x <= 0:
        return -x / 2 - 3
    elif x <= 3:
        #защищает от микроошибок округления float под корнем
        return -math.sqrt(max(0.0, 9 - x**2))
    else:
        return math.sqrt(max(0.0, 9 - (x - 6)**2))

def draw_graph():
    """Функция для пошаговой отрисовки графика"""
    t.pencolor("blue")
    t.pensize(3)
    
    #диапазон отрисовки по оси X (например, от -8 до 9)
    x_start = -8.0
    x_end = 9.0
    dx = 0.05  #Маленький шаг для гладкости линий окружностей
    
    y_start = calculate_y(x_start)
    t.penup()
    t.goto(x_start * SCALE, y_start * SCALE)
    t.pendown()
    
    x = x_start
    while x <= x_end:
        y = calculate_y(x)
        t.goto(x * SCALE, y * SCALE)
        x += dx

draw_axes()
draw_graph()

screen.mainloop()
