"""(Е. Джобс) Геннадий создает мультипликационный ролик, где каждый кадр - отдельно
отрисованная картинка. Известно, что каждая картинка имеет разрешение 640х480 пикселей и
цветовую палитру в 2^16 = 65536 цветов. Каждый пиксель кодируется с помощью минимально
возможного и одинакового для всех пикселей количества бит. Картинки записываются одна за
другой без разделителей и заголовков файла. Частота смены кадров в конечном ролике - 24
кадра/сек. В качестве звукового сопровождения выбран формат стерео с глубиной кодирования
10 бит и частотой дискретизации 40 кГц. Найдите размер мультфильма в МБайтах, если известно,
что его длительность 5 минут. В качестве ответа укажите число минимальное целое количество
Мбайт достаточное для хранения такого файла."""
I1 = 16 * 640 * 480 * 24
I2 = 40000 * 10 * 2
I = (I1 + I2) * 300 // 1024 // 1024 // 8
print(I + 1)