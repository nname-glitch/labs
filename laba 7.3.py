import turtle

#граф окно
screen = turtle.Screen()
screen.title("Лабораторная работа №7: График функции через ряд (Задание 3)")
screen.setup(width=800, height=600)
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)  #скорость рисования
t.hideturtle()

#Кэфы масштабирования (1 единица = 50 пикселей на экране)
SCALE = 50
EPSILON = 0.001  # Точность 10^-3 по условию задачи

def draw_axes():
    """Отрисовка осей координат и разметки"""
    t.pencolor("gray")
    t.pensize(1)
    
    # Ось X
    t.penup()
    t.goto(-350, 0)
    t.pendown()
    t.goto(350, 0)
    
    # Ось Y
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
    
    #Засечки и числа на осях (от -6 до 6)
    for i in range(-6, 7):
        if i == 0:
            continue
            
        #засечки x
        t.penup()
        t.goto(i * SCALE, -5)
        t.pendown()
        t.goto(i * SCALE, 5)
        t.penup()
        t.goto(i * SCALE - 5, -20)
        t.write(str(i), font=("Times New Roman", 9, "normal"))
        
        #засечки y
        t.penup()
        t.goto(-5, i * SCALE)
        t.pendown()
        t.goto(5, i * SCALE)
        t.penup()
        t.goto(-20, i * SCALE - 5)
        t.write(str(i), font=("Times New Roman", 9, "normal"))

def calculate_series_y(x):
    """Вычисление значения функции через сумму ряда с точностью EPSILON"""
    # Защита от деления на ноль
    if abs(x) <= 0.0001:
        return None
        
    s = 0
    n = 0
    t_term = 1
    
    #Алгоритм расчёта ряда
    while abs(t_term) >= EPSILON:
        # Ограничиваем рост n из-за overflow 
        if n > 500:
            break
        t_term = 2 / ((2 * n + 1) * (x ** (2 * n + 1)))
        s += t_term
        n += 1
        
    return s

def draw_graph_line(x_start, x_end, step=0.02):
    """Отрисовка непрерывной ветви графика на заданном интервале x"""
    t.pencolor("blue")
    t.pensize(2.5)
    
    x = x_start
    first_point = True
    
    while x <= x_end:
        y = calculate_series_y(x)
        
        if y is not None:
            #Ограничиваем рисование по высоте окна
            if -5 <= y <= 5:
                if first_point:
                    t.penup()
                    t.goto(x * SCALE, y * SCALE)
                    t.pendown()
                    first_point = False
                else:
                    t.goto(x * SCALE, y * SCALE)
                    
        x = round(x + step, 4)

# Порядок выполнения программы
draw_axes()
# Рисуем левую ветвь графика
draw_graph_line(-5.0, -1.05)
# Рисуем правую ветвь графика
draw_graph_line(1.05, 5.0)

screen.mainloop()