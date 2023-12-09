"""(Е. Джобс) Для хранения сжатого растрового изображения выделено З Мбайт. Для каждого
пикселя записывается информация о его цвете и уровне прозрачности. Как информация о цвете,
так и информация об уровне прозрачности записываются с помощью одинакового количества бит
для каждой части. После кодирования информации о каждом пикселе изображение сжимается.
Сжатое изображение меньше исходного на 20%. Определите, какое максимальное количество
уровней прозрачности может быть у изображения размером 1080х920, если известно, что
используется цветовая палитра, содержащая 1 миллион цветов."""
I = 3 * 2**23
i = I // (0.8 * 1080 * 920)
i2 = 0
e = 1000000
while e != 0:
    i2 += 1
    e //= 2
print(2**(i-i2))