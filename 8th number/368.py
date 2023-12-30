"""Сколько существует чисел, пятнадцатеричная запись которых содержит 5 разрядов,
причём разряды, кратные 2 и кратные 3, чередуются? Например, число 40068 подходит под
описание, число 40086 - нет."""
from itertools import *

ans = 0
for i in product('012345', repeat=7):
    i = ''.join(i)
    if i[0] != '0':
        if i.count('2') == 1:
            i = i.replace('0', 'x')
            i = i.replace('4', 'x')
            if 'x2' not in i and '2x' not in i:
                ans += 1
print(ans)
