"""Для хранения произвольного растрового изображения размером 800х1024 пикселей отведено
300 Кбайт памяти без учёта размера заголовка файла. Для кодирования цвета каждого пикселя
используется одинаковое количество бит, коды пикселей записываются в файл один за другим без
промежутков. При сохранении данные сжимаются, размер итогового файла после сжатия
становится на 40% меньше исходного. Какое максимальное количество цветов можно
использовать в изображении?"""
i = (300 * 2**13) // (800 * 1024 * 0.6)
print(2**i)
