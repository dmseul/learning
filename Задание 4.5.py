x = input('Введите число:')
try:
    x = float(x)
    print(x)
except ValueError:
    print('Ошибка ввода. Нужно ввести число!')
