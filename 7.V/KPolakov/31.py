"""Сколько секунд потребуется модему, передающему сообщения со скоростью 28800 бит/с, чтобы
передать растровое изображение размером 800 х 600 пикселей, при условии, что в палитре 2^24
цветов?"""
v = 28800
xy = 8 * 60000
i = 24
print(xy * i / v)