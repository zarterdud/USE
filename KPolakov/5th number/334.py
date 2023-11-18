'''
334)	(ЕГЭ-2023) На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом:
1. Строится троичная запись числа N.

2. Если число N делится на 3, к троичной записи слева приписывается 1, а справа – 02;
иначе остаток от деления числа на 3 умножается на 4, переводится в троичную систему и дописывается в конец троичной записи.

3. Полученная таким образом запись является троичной записью искомого числа R.
Например, для числа 11 троичная запись 102 3 преобразуется в запись 10222 3 = 107,
для числа 12 троичная запись 1103 преобразуется в 1110023 = 353. Укажите максимальное значение N,
после обработки которого с помощью этого алгоритма получается число R, меньшее чем 199.
'''
def transletion(n):
  n_ter = ''
  while n > 0:
    n_ter += str(n % 3)
    n //= 3
  return n_ter[::-1]
ans = []
for n in range(1, 1000 + 1):
  n_ter = transletion(n)
  if n_ter[-1] == '0':
    n_ter = '1' + n_ter + '02'
  else:
    n_ter = n_ter + str(transletion((int(n_ter, 3) % 3) * 4))
  r_dec = int(n_ter, 3)
  if r_dec < 199:
    ans.append(n)
print(max(ans))
