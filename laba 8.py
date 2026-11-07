import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

class Lab8App:
    def __init__(self, root):
        self.root = root
        self.root.title("Лабораторная работа №8: Графики функций (Вариант 11)")
        self.root.geometry("900x650")
        self.root.minsize(700, 500)
        
        # Главный контейнер
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill="both", expand=True)
        
        # Левая панель управления
        control_frame = ttk.LabelFrame(main_frame, text=" Входные данные ")
        control_frame.pack(side="left", fill="y", padx=10, pady=10)
        
        # Поля ввода параметров (Ограничение по умолчанию: x > 0)
        ttk.Label(control_frame, text="X начальное (X > 0):").pack(anchor="w", padx=5, pady=2)
        self.entry_x_start = ttk.Entry(control_frame)
        self.entry_x_start.insert(0, "0.2")
        self.entry_x_start.pack(fill="x", padx=5, pady=2)
        
        ttk.Label(control_frame, text="X конечное:").pack(anchor="w", padx=5, pady=2)
        self.entry_x_end = ttk.Entry(control_frame)
        self.entry_x_end.insert(0, "5.0")
        self.entry_x_end.pack(fill="x", padx=5, pady=2)
        
        ttk.Label(control_frame, text="Шаг dx:").pack(anchor="w", padx=5, pady=2)
        self.entry_dx = ttk.Entry(control_frame)
        self.entry_dx.insert(0, "0.05")
        self.entry_dx.pack(fill="x", padx=5, pady=2)
        
        ttk.Label(control_frame, text="Точность ряда (eps):").pack(anchor="w", padx=5, pady=2)
        self.entry_eps = ttk.Entry(control_frame)
        self.entry_eps.insert(0, "0.001")
        self.entry_eps.pack(fill="x", padx=5, pady=2)
        
        ttk.Label(control_frame, text="Параметр b:").pack(anchor="w", padx=5, pady=2)
        self.entry_b = ttk.Entry(control_frame)
        self.entry_b.insert(0, "0.5")
        self.entry_b.pack(fill="x", padx=5, pady=2)
        
        # Кнопка расчета
        btn_calc = ttk.Button(control_frame, text="Построить графики", command=self.plot_graphs)
        btn_calc.pack(fill="x", padx=5, pady=15)
        
        # Легенда
        legend_frame = ttk.LabelFrame(control_frame, text=" Легенда ")
        legend_frame.pack(fill="x", padx=5, pady=10)
        
        lbl_y = tk.Label(legend_frame, text="—— y(x) (Ряд Вариант 11)", fg="blue", font=("Arial", 10, "bold"))
        lbl_y.pack(anchor="w", padx=5, pady=2)
        
        lbl_z = tk.Label(legend_frame, text="—— z(x) (ln x + b)", fg="red", font=("Arial", 10, "bold"))
        lbl_z.pack(anchor="w", padx=5, pady=2)
        
        # Правая часть — Холст для рисования
        self.canvas = tk.Canvas(main_frame, bg="white", highlightthickness=1, highlightbackground="lightgray")
        self.canvas.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        
        # Связываем изменение размера окна с автоматической перерисовкой графика
        self.canvas.bind("<Configure>", lambda event: self.plot_graphs())

    def calculate_y(self, x, eps):
        """Вычисление y(x) через ряд Тейлора для Варианта 11"""
        if x <= 0:
            return None
        s = 0
        n = 0
        t_term = 1.0
        # Базовый множитель (x-1)/(x+1)
        base = (x - 1) / (x + 1)
        
        while abs(t_term) >= eps:
            if n > 500:  #Защита от бесконечного цикла
                break
            #Вычисляем текущий член ряда
            t_term = (base ** (2 * n + 1)) / (2 * n + 1)
            s += t_term
            n += 1
        return 2 * s

    def calculate_z(self, x, b):
        """Вычисление аналитической функции z(x) = ln x + b"""
        if x <= 0:
            return None
        try:
            return math.log(x) + b
        except ValueError:
            return None

    def plot_graphs(self):
        self.canvas.delete("all")
        
        #Считывание параметров из интерфейса
        try:
            x_start = float(self.entry_x_start.get())
            x_end = float(self.entry_x_end.get())
            dx = float(self.entry_dx.get())
            eps = float(self.entry_eps.get())
            b = float(self.entry_b.get())
        except ValueError:
            return  #Игнор до ввода корректных чисел
            
        #Проверка x должен быть строго больше 0
        if x_start <= 0 or x_end <= 0:
            self.canvas.create_text(250, 30, text="Ошибка: Обе функции определены только при X > 0", fill="red")
            return

        #Размеры холста
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        if w < 10 or h < 10: 
            return
            
        #Сбор точек для авто масштаба
        y_points = []
        z_points = []
        x_vals = []
        
        curr_x = x_start
        while (dx > 0 and curr_x <= x_end) or (dx < 0 and curr_x >= x_end):
            y_val = self.calculate_y(curr_x, eps)
            z_val = self.calculate_z(curr_x, b)
            
            if y_val is not None and z_val is not None:
                x_vals.append(curr_x)
                y_points.append(y_val)
                z_points.append(z_val)
            curr_x += dx

        if not x_vals:
            return

        #Поиск мин и макс значений для автомасштаба сетки
        valid_y = y_points + z_points
        min_x, max_x = min(x_vals), max(x_vals)
        min_y, max_y = min(valid_y), max(valid_y)
        
        if max_x == min_x: max_x += 1
        if max_y == min_y: max_y += 1
        
        padding = 40
        
        #перевоа математических координат в пиксели
        def get_cx(x_m):
            return padding + (x_m - min_x) / (max_x - min_x) * (w - 2 * padding)
            
        def get_cy(y_m):
            return (h - padding) - (y_m - min_y) / (max_y - min_y) * (h - 2 * padding)

        #Рисуем горизонтальную ось Y = 0
        if min_y <= 0 <= max_y:
            cy_zero = get_cy(0)
            self.canvas.create_line(padding, cy_zero, w - padding, cy_zero, fill="darkgray", width=1.5)
        
        #Рисуем вертикальную ось X = 0
        if min_x <= 0 <= max_x:
            cx_zero = get_cx(0)
            self.canvas.create_line(cx_zero, padding, cx_zero, h - padding, fill="darkgray", width=1.5)

        #Отрисовка подписей градаций осей
        self.canvas.create_text(get_cx(min_x), h - padding + 15, text=f"{min_x:.2f}", font=("Arial", 9))
        self.canvas.create_text(get_cx(max_x), h - padding + 15, text=f"{max_x:.2f}", font=("Arial", 9))
        self.canvas.create_text(padding - 20, get_cy(min_y), text=f"{min_y:.2f}", font=("Arial", 9))
        self.canvas.create_text(padding - 20, get_cy(max_y), text=f"{max_y:.2f}", font=("Arial", 9))
        
        #названия осей
        self.canvas.create_text(w - 20, h - padding, text="X", font=("Arial", 10, "bold"))
        self.canvas.create_text(padding, 20, text="Y", font=("Arial", 10, "bold"))

        #Отрисовка линий графиков двух функций
        for i in range(len(x_vals) - 1):
            cx1 = get_cx(x_vals[i])
            cx2 = get_cx(x_vals[i+1])
            
            #График синий
            cy1_y = get_cy(y_points[i])
            cy2_y = get_cy(y_points[i+1])
            self.canvas.create_line(cx1, cy1_y, cx2, cy2_y, fill="blue", width=2)
                
            #График красный
            cy1_z = get_cy(z_points[i])
            cy2_z = get_cy(z_points[i+1])
            self.canvas.create_line(cx1, cy1_z, cx2, cy2_z, fill="red", width=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = Lab8App(root)
    root.mainloop()
