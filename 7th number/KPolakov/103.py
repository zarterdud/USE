"""(Досрочный ЕГЭ-2022) Для хранения произвольного растрового изображения размером 486х720
пикселей отведено 80 Кбайт памяти без учёта размера заголовка файла. Для кодирования цвета
каждого пикселя используется одинаковое количество бит, коды пикселей записываются в файл
один за другим без промежутков. При сохранении данные сжимаются, размер итогового файла
после сжатия становится на 15% меньше исходного. Какое максимальное количество цветов
можно использовать в изображении?"""
# I = x * y * i
i = (80 * 2**13 * 0.85) // (486 * 720)
print(i)