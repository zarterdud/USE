from math import pi

"""(Д. Статный) На фабрике производят глобусы диаметром 40 см, на которые требуется нанести
карту. Изображение поверхности планеты, которое нужно наносить на глобус, сохранено с
инейным разрешением 300 ppi с использованием 2^24 цветов. Сколько Мбайт потребуется для
хранения карты? Поверхность глобуса можно принять за сферу, площадь поверхности сферы
вычисляется по формуле S = 4pR^2, где R - радиус сферы. Примечание: 1 дюйм = 2,54 см. В ответе
введите целое число."""
i = 24
S = 4 * pi * 20**2
t = 300**2
sm2 = 2.54 * 2.54
tochki = S * t // sm2
I = tochki * i / (2**23)
print(int(I) + 1)
