"""Стереоаудиофайл передается со скоростью 32000 бит/с. Файл был записан с такими параметрами:
глубина кодирования - 16 бит на отсчет, частота дискретизации - 48000 отсчетов в секунду, время
записи - 90 с. Сколько минут будет передаваться файл?"""
v = 32000
B = 16
f = 48000
t = 90
print(2 * B * f * t / v / 60)
