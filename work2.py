# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.

class ZeroError(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y

try:
    x = int(input(f'Введите число, которое собираетесь разделить: '))
    y = int(input(f'Введите число, которое собираетесь разделить: '))
    if not y:
        print(f'Нельзя делить на ноль.')
    else:
        print(f'Результат {x / y}')
except ValueError:
    print(f'Вы ввели не число.')


