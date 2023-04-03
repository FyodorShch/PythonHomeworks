# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

ma = int(input()) #Ввод максимума
mi = int(input()) #Ввод минимума
lst = []
result = []
n = int(input()) #Ввод количества элементов списка

for i in range(n):
    lst.append(input())

for i in range(n):
    if int(lst[i]) <= ma and int(lst[i]) >= mi:
        result.append(i)

print(result)