# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.

class Error(Exception):
    def __init__(self, numbers):
        self.numbers = numbers

total_list = []
while True:
    value = input('Введите элемент для добавления в список или stop для завершения: ')
    if value == 'stop':
        print(f'Список на момент завершения{total_list}')
        break

    try:
        if not value.i():
            raise Error('No!')
        total_list.append(int(value))
    except Error as err:
        print('Вы ввели не число')