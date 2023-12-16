"""У Васи есть доступ к Интернет по высокоскоростному одностороннему радиоканалу,
обеспечивающему скорость получения им информации 2^17 бит в секунду. У Пети нет скоростного
доступа в Интернет, но есть возможность получать информацию от Васи по низкоскоростному
телефонному каналу со средней скоростью 2^16 бит в секунду. Петя договорился с Васей, что тот
будет скачивать для него данные объемом 8 Мбайт по высокоскоростному каналу и
ретранслировать их Пете по низкоскоростному каналу. Компьютер Васи может начать
ретрансляцию данных не раньше, чем им будут получены первые 1024 Кбайт этих данных. Каков
минимально возможный промежуток времени (в секундах), с момента начала скачивания Васей
данных, до полного их получения Петей? В ответе укажите только число, слово «секунд» или
букву «с» добавлять не нужно."""
I = 8 * 2**23
t0 = 1024 * 2**13 / 2**17
t1 = I / 2**16
t = t0 + t1
print(t)