"""Петя составляет пятибуквенные слова из букв Т, И, М, А, Ш, Е, В, С, К. Он выбирает
только те слова, в которых буква Ш не стоит рядом с гласной и с буквой В. Сколько таких слов
может составить Петя?"""
from itertools import product

count = 0

for x in product("ТИМАШЕВСК", repeat=5):
    word = "".join(x)
    value = 0
    for i in word:
        if all(VT not in word for VT in ["ИШ", "ШИ", "АШ", "ША", "ЕШ", "ШЕ"]):
            value += 1
    if value >= 3:
        count += 1

print(count)
