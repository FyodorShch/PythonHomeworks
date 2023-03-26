# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X. 
# Пользователь вводит это число с клавиатуры, список можно считать заданным. 
# Введенное число не обязательно содержится в списке.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
# Output: 10

list = []

for i in range(5):
    n = int(input())
    list.append(n)

print(list)

closerx = 0
x = int(input())
mindifference = 100000000

for i in range(len(list)):
    if abs(x - list[i])<mindifference:
        closerx = list[i]
        mindifference = abs(x - list[i])

print(f"Input: {list}, x = {x}\nOutut: {closerx}")