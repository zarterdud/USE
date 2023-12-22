"""33) (А.Н. Носкин) Все 5-буквенные слова, составленные из букв П, О, Р, Т, записаны в алфавитном
порядке и пронумерованы. Вот начало списка:
1 ООООО
2 ООООП
3 ООООР
4 ООООТ
5 ОООПО
……
Какое количество слов находятся между словами ТОПОР и РОПОТ (включая эти слова)?"""
import itertools

ans = 0
e = 0
for i in itertools.product(['О', 'П', 'Р', 'Т'], repeat=5):
    i = ''.join(i)
    if e == 1:
        ans += 1
    if i == 'ТОПОР':
        break
    if i == 'РОПОТ':
        ans += 1
        e = 1
print(ans)
