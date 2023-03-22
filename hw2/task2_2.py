# 2.2[12]: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y ≤ 1000),
# а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# Примеры/Тесты:
# 4 4 -> 2 2
# 5 6 -> 2 3

from math import sqrt

s = int(input())
p = int(input())

if p % s == 0:
    x = y = s/2
    print(f"{x}, {y}")
else:
    a = s ** 2 - 4*p
    x = (-s + sqrt(a))/-2
    y = (-s - sqrt(a))/-2
    print(x, y)