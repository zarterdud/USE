'''
186)	Автомат обрабатывает натуральное число N < 256 по следующему алгоритму:
1) Строится восьмибитная двоичная запись числа N.
2) Инвертируются все разряды исходного числа, кроме последней единицы и стоящих за ней нулей (0 заменяется на 1, 1 на 0).
3) Полученное число переводится в десятичную систему счисления.
Чему равен результат работы алгоритма для N = 211?
'''

n = 211
n_bin = bin(n)[2:]
ans = ''
for i in range(len(str(n_bin)) - 1):
  if n_bin[i] == '1':
    ans += '0'
  else:
    ans += '1'
ans += "1"
print(int(ans, 2))
