'''
173)	(А.М. Кабанов, Тольятти)  Автомат обрабатывает натуральное число N (1≤N≤255) по следующему алгоритму:
1) Строится восьми битная двоичная запись числа N.
2) Удаляется последняя цифра двоичной записи.
3) Запись «переворачивается», то есть читается справа налево.
4) Полученное число переводится в десятичную запись и выводится на экран.
Каково наибольшее число, меньшее 100, которое после обработки автоматом не изменится?
'''
ans = []
for i in range(1, 100):
  a = str(bin(i)[2:])
  a = ('0' * (8 - len(a)) + a)[:-1]
  # print(a)
  b = int(a[::-1], 2)
  if b == i:
    ans.append(i)
print(max(ans))
