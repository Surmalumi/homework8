# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».

class Date:

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def my_str(cls, date_as_str):
        day, month, year = map(int, date_as_str.split("/"))
        date = cls(day, month, year)
        print(cls, date_as_str)
        return date

    @staticmethod
    def date_valid(date_as_str):
        day, month, year = map(int, date_as_str.split("/"))
        if day <= 31 and day != 0 and month <=12 and month !=0 and year >= 0:
            print(date_as_str)
            return day, month, year
        else:
            print("Error in dates!")


d = "10/05/2010"
d_1 = "01/12/-1500"
date_1 = Date.my_str(d)
date_2 = Date.my_str(d_1)
date_valid = Date.date_valid(d)
date_valid_1 = Date.date_valid(d_1)
