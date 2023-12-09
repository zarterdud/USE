"""(Е. Джобс) Для хранения растрового изображения размером 1200х1800 пикселей отведено
1 Мбайт памяти. Для кодирования цвета каждого пикселя используется одинаковое количество
бит, коды пикселей записываются в файл один за другим без промежутков. После сохранения
информации о пикселях изображение сжимается. После сжатия изображение имеет размер,
равный 75% от исходного. К сжатому изображению дописывается заголовок файла размером 40
Кбайт. Какое максимальное количество цветов можно использовать в изображении?"""
i = (2**10 - 40) * 2**13 // (1200 * 1800 * 0.75)
print(2**i)
