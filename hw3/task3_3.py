# 3.3[20]: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, 
# либо только русские буквы, и заранее известно какой алфавит надо использовать.

# Примеры/Тесты:
# Input:   ноутбук
# Output:  12

# Input:   notebook
# Output:  14

scores = {**dict.fromkeys("aeioulnstr", 1), **dict.fromkeys("dg", 2), **dict.fromkeys("bcmp", 3), **dict.fromkeys("fhvwy", 4), **dict.fromkeys("k", 5), **dict.fromkeys("jx", 8), **dict.fromkeys("qz", 10)}
scores1 = {**dict.fromkeys("авеинорст", 1), **dict.fromkeys("дклмпу", 2), **dict.fromkeys("бгёья", 3), **dict.fromkeys("йы", 4), **dict.fromkeys("жзхцч", 5), **dict.fromkeys("шэю", 8), **dict.fromkeys("фщъ", 10)}
wl = str(input())
word = str(input())
count = 0

if wl == 'rus':
    for i in word:
        count = count + scores1[i]
else:
    for i in word:
        count = count + scores[i]

print(f"Input: {word}\nOutput: {count}")