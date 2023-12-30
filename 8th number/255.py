"""Сколько существует чётных натуральных чисел, у которых восьмеричная запись
состоит из пяти цифр, начинается с цифры 7 и содержит ровно одно из сочетаний 65 или 56, но не
оба одновременно."""
import itertools

alphabet = "01234567"
cet = "0246"
necet = "1357"
ar = itertools.permutations(alphabet, 5)
arl = []
for e in ar:
    arl.append(list(e))
count = 0
for e in arl:
    flag = True
    for i in range(len(e) - 1):
        if (
            (e[i] in cet and e[i + 1] in cet)
            or (e[i] in necet and e[i + 1] in necet)
            or e[0] == "0"
            or e.count("1") != 0
        ):
            flag = False
    if flag:
        count += 1
print(count)
