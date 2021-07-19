duration = int(input('Введите количество секунд '))
print(duration, 'сек равно')
result = ''
_duration = duration // 86400  # дни
if _duration > 0:
    result += str(_duration) + ' дн '
_duration = duration % 86400 // 3600  # часы
if _duration > 0:
    result += str(_duration) + ' час '
_duration = duration % 3600 // 60  # минуты
if _duration > 0:
    result += str(_duration) + ' мин '
_duration = duration % 60  # секунды
if _duration > 0:
    result += str(_duration) + ' сек '
print(result)