"""125) (А.Н. Носкин) Петя составляет семибуквенные слова перестановкой букв слова ТРАТАТА. Сколько
всего различных слов может составить Петя?"""
import itertools

ans = set()
for i in itertools.permutations('ТРАТАТА'):
    i = ''.join(i)
    ans.add(i)
print(len(ans))
