duration = int(input('Введите время в секундах: '))
times = (60 * 60 * 24)
days = duration // times
hours = (duration - days * times) // (60 * 60)
minutes = (duration - days * times - hours * (60 * 60)) // 60
seconds = duration - days * times - hours * (60 * 60) - minutes * 60
print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')