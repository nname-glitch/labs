n = int(input("Введите кол. n " ))
truly = []
#добавление в список цифры в конец списка
for i in range(n):
    truly.append(int(input("Введите эл: " )))
#сложение отриц чисел
s = 0
for i in range(n):
    if truly[i] < 0:
        s = s + truly[i]
print("сумма отрицательных эл: ", s)

bigbon = truly.index(max(truly))
gnome = truly.index(min(truly))
#Сортиворка индексов по порядку
if bigbon > gnome:
    t = bigbon
    bigbon = gnome
    gnome = t
#сложение между макс числом и мин числом
p = 1
for i in range(bigbon + 1, gnome):
    p = p * truly[i]
print('Произведение:', p)

truly.sort()
print('массив по возрастанию:', truly)