"""89) На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R
следующим образом.
1) Строится двоичная запись числа N.
2) К этой записи дописывается справа бит чётности: О, если в двоичном коде числа N было чётное
число единиц, и 1, если нечётное.
З) К полученному результату дописывается ещё один бит чётности.
Полученная таким образом запись (в ней на два разряда больше, чем в записи исходного числа N)
является двоичной записью искомого числа R. Укажите минимальное число N, после обработки
которого с помощью этого алгоритма получается число, большее, чем 121, В ответе это число
запишите в десятичной системе."""
ans = int("1111111", 2)
print(ans)
