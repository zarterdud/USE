"""87) (А.Н. Носкин) Все пятибуквенные слова, составленные из букв В, Е, Н, О, К, записаны в алфавитном
порядке и пронумерованы, начиная с 1 Начало списка выглядит так:
1 ВВВВВ
2 ВВВВЕ
3 ВВВВК
4 ВВВВН
5 ВВВВО
6 ВВВЕВ
…
Под каким номером в списке идёт последнее слово, в котором буквы Н и К встречаются ровно по
два раза?"""
import itertools

ans = 0
e = 0
for i in itertools.product('ВЕКНО', repeat=5):
    e += 1
    if i.count('Н') == 2 and i.count('К') == 2:
        ans = e
print(ans)
