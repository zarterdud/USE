"""(А. Богданов) При кодировании растрового изображения размером 1920х1080 пикселей на
каждый пиксель отводится несколько бит для кодирования цвета и один бит прозрачности. Коды
пикселей записываются в файл один за другим без промежутков. Затем изображение сжимается
на 20%. Какое максимальное количество цветов (без учета степени прозрачности) можно
использовать в изображении, если для его хранения отведено 1215 Кбайт памяти без учёта
размера заголовка файла?"""
I = 1215 * 2**13 * 1.2
print(2**(I // 1920 // 1080))
