percent = int(input('Введите число процента: '))
if percent == 1:
    word = 'Процент'
elif percent <= 4:
    word = 'Процента'
else:
    word = 'Процентов'
print(percent,word)