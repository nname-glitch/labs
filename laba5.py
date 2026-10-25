import random
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
    return  count      

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
def print_matrix(matrix):
    for row in matrix:
        for num in row:
            print(num, end='\t')
        print()
rows = int(input("Введите количество строк матрицы: "))
cols = int(input("Введите количество столбцов матрицы: "))         
                                       
my_matrix = []
# цикл рандомных цифр в строке и столбце
for i in range(rows):
    row = []
    for j in range(cols):
        num = random.randint(-10,10)
        row.append(num)
    my_matrix.append(row)
print("Сгенерированная матрица:")
print_matrix(my_matrix)
print()

# Вызов первой функции
res1 = count_rows_without_zeros(my_matrix)
print("1. Количество строк без нулей:", res1)

# Вызов второй функции
res2 = max_duplicate(my_matrix)
print("2. Максимальное повторяющееся число:", res2)        