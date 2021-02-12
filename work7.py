# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.

class ComplexNumbers:

    def __init__(self, x, y, *args):
        self.x = x
        self.y = y
        self.z = "x + y * i" # i-мнимая единица


    def __str__(self):
        return f'z = {self.x} + {self.y} * i'


    def __add__(self, other):
        print(f'Сумма чисел z1 и z1 равна:')
        return f'x = {self.x + other.x} + {self.y + other.y} * i'


    def __mul__(self, other):
        print(f'Произведение чисел z1 и z2 равно:')
        return f'c = {self.x * other.x} - {self.y * other.y}  * i' # вроде так, но кажется я все-таки запуталась в формуле.


z_1 = ComplexNumbers(5, 2)
z_2 = ComplexNumbers(1, 3)
print(z_1 + z_2)
print(z_1 * z_2)
# Надо будет попробовать с модулем Math решить.