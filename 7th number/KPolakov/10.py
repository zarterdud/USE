"""10) Какой минимальный объём памяти (в Кбайт) нужно зарезервировать, чтобы можно было
сохранить любое растровое изображение размером 128 на 128 пикселов при условии, что в
изображении могут использоваться 256 различных цветов? В ответе запишите только целое число,
единицу измерения писать не нужно."""
# I = x * y * i
# 256 = 2 ** 8
x = 128 ** 2 * 8
print(x // 2 ** 13)