"""Марат составляет 8-буквенные коды из букв, входящих в слово ГАЛАКТИКА. Первая
буква кода должна быть согласной, а последняя — гласной. Код НЕ должен содержать ни одной
пары соседних букв, которые следуют друг за другом в русском алфавите в таком же порядке
(например, "АБ" или "ЮЯ"). Сколько различных кодов может составить Марат?"""
import itertools
alphabet = "ГАЛАКТИКА"
vol = "АИ"
con = "ГЛКТ"
ar = itertools.permutations(alphabet, 8)
arl = []
for e in ar:
    arl.append(list(e))
a = set()
for e in arl:
    flag = True
    s = ""
    for i in range(len(e)-1):
        s += e[i]
        if (e[i] in vol and e[i+1] in vol) or (e[i] in con and e[i+1] in con):
            flag = False
    if flag:
        a.add(s)
print(len(a))
