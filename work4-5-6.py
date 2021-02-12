# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.

class Warehouse:
    print("Склад оргтехники")

class OfficeEquipment:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.warehouse_full = []
        self.warehouse = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'


    def info(self):

        try:
            unit = input(f'Введите наименование ')
            unit_price = int(input(f'Введите цену за ед '))
            unit_qty = int(input(f'Введите количество '))
            product = {'Модель устройства': unit, 'Цена за ед': unit_price, 'Количество': unit_qty}
            self.my_unit.update(product)
            self.warehouse.append(self.my_unit)
            print(f'Текущий список -\n {self.warehouse}')
        except:
            return f'Ошибка ввода данных'

        print(f'Введите x для завершения')
        x = input(f' ')
        if x:
            self.warehouse_full.append(self.warehouse)
            print(f'На складе -\n {self.warehouse_full}')
            return f'Выход'
        else:
            return OfficeEquipment.info(self)


class Printer(OfficeEquipment):

    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(OfficeEquipment):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(OfficeEquipment):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'



unit_1 = Printer('', 1000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.info())
print(unit_2.info())
print(unit_3.info())