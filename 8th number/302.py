"""302) (М. Байрамгулов) Ваня составляет 6-буквенные слова из букв слова КОМПЬЮТЕР так, что в них
можно убрать три буквы и получить слово КОТ. Сколько различных слов может составить Ваня?"""
from itertools import product


def check(v):
    k, o, t = 0, 0, 0
    for i in v:
        if i == "K":
            k = 1
        elif i == "O" and k == 1:
            o = 1
        elif i == "T" and o == 1:
            t = 1
    return k * o * t


a = ["K", "O", "M", "P", "`", "U", "T", "E", "R"]
b = list(product(a, repeat=6))
c = 0
for i in b:
    c += check(i)
print(c)
