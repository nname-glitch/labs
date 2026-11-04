from math import *

# Функция из лабы 5
def count_rows_without_zeros(matrix):
    count = 0
    for row in matrix:
        has_zero = 0
        for num in row:
            if num == 0:
                has_zero = 1
                break
        if has_zero == 0:
            count += 1
    return count      

# Функция из лабы 5
def max_duplicate(matrix):
    all_elemets = [] 
    for row in matrix:
        for num in row:
            all_elemets.append(num)
    duplicates = []
    for num in all_elemets:
        if all_elemets.count(num) > 1:
            if num not in duplicates:
                duplicates.append(num)
    if len(duplicates) == 0:
        return "нет повторений"
    max_val = duplicates[0]
    for num in duplicates:
        if num > max_val:
            max_val = num
    return max_val

def main():
    import os
    # Находим точный путь к папке
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    file_in = os.path.join(current_dir, "input.txt")
    file_out = os.path.join(current_dir, "output.txt")
    
    # пробуем прочитать файл
    try:
        with open(file_in, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Ошибка! Не нашли файл {file_in}. Положи его в папку с кодом!")
        return
    except Exception as e:
        print(f"Что-то пошло не так при открытии файла: {e}")
        return

    # Проверяем хватает ли строчек в файле
    if len(lines) < 3:
        print("Ошибка! В файле слишком мало строк, не хватает данных.")
        return

    try:
        a = float(lines[0].strip())
        
        truly = []
        for x in lines[1].strip().split():
            truly.append(int(x))
            
        my_matrix = []
        for line in lines[2:]:
            cleaned = line.strip()
            if cleaned:
                row = []
                for x in cleaned.split():
                    row.append(int(x))
                my_matrix.append(row)
                
    except ValueError:
        print("Ошибка! В файле какой-то левый текст вместо чисел. Проверь данные.")
        return

    z1 = 2 * (sin(3 * pi - 2 * a))**2 * (cos(5 * pi + 2 * a))**2
    z2 = 1/4 - 1/4 * sin(5/2 * pi - 8 * a)
 
    n = len(truly)
    s = 0
    for i in range(n):
        if truly[i] < 0:
            s = s + truly[i]

    bigbon = truly.index(max(truly))
    gnome = truly.index(min(truly))
    
    if bigbon > gnome:
        t = bigbon
        bigbon = gnome
        gnome = t

    p = 1
    for i in range(bigbon + 1, gnome):
        p = p * truly[i]
        
    # Сортируем массив 
    truly_sorted = sorted(truly)

    
    res1 = count_rows_without_zeros(my_matrix)
    res2 = max_duplicate(my_matrix)

    # записываем все в оутпут
    try:
        with open(file_out, "w", encoding="utf-8") as out:
            out.write("РЕЗУЛЬТАТЫ ОБРАБОТКИ ДАННЫХ ИЗ ФАЙЛА (ЛАБА №6)\n")
            
            out.write("1. Результаты из Лабораторной работы №1:\n")
            out.write(f"Входной параметр a = {a}\n")
            out.write(f"Вычисленный z1 = {z1}\n")
            out.write(f"Вычисленный z2 = {z2}\n\n")
            
            out.write("2. Результаты из Лабораторной работы №4:\n")
            out.write(f"Считанный массив truly: {truly}\n")
            out.write(f"Сумма отрицательных элементов: {s}\n")
            out.write(f"Произведение между мин и макс: {p}\n")
            out.write(f"Массив по возрастанию: {truly_sorted}\n\n")
            
            out.write("3. Результаты из Лабораторной работы №5:\n")
            out.write("Считанная матрица my_matrix:\n")
            for row in my_matrix:
                for num in row:
                    out.write(f"{num}\t")
                out.write("\n")
            out.write(f"Количество строк без нулей: {res1}\n")
            out.write(f"Максимальное повторяющееся число: {res2}\n")
            
            
        print(f"Всё готово! Результаты легли в файл: {file_out}")
        
    except Exception as e:
        print(f"Не удалось записать отчет в файл: {e}")

if __name__ == "__main__":
    main()
