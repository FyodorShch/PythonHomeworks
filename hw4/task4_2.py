# 4.2[24]: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом. На входе задано количество ягод на каждом кусте. Не обязательно вводить их с клавиатуры, можно задать непосредственно в коде программы

# Примеры/Тесты:
# Input1: 1, 2, 3, 4, 5, 6, 7, 8
# Output1: Макс. кол-во ягод 21, собрано для куста 7

# Input1: 11, 92, 1, 42, 15, 12, 11, 81
# Output1: Макс. кол-во ягод 184, собрано для куста 1

list1 = [11, 92, 1, 42, 15, 12, 11, 81]
total_sum = 0
for i in range(len(list1)):
    i_next = i + 1 if i != len(list1) - 1 else i - len(list1) + 1
    sum_current = list1[i - 1] + list1[i] + list1[i_next]
    if sum_current > total_sum:
        total_sum = sum_current
        find_idx = i
print(f"Макс. кол-во ягод {total_sum}, собрано для куста {find_idx+1}")
