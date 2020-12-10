"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""
import datetime


class MyDate:
    str_date = "dd-mm-yyyy"

    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def extract_date_numbers(cls, param):
        return int("".join(param.split("-")))

    @staticmethod
    def is_valid_date(param):
        try:
            datetime.datetime.strptime(param, "%d-%m-%Y")
            print(f"This is the correct date format.")
            return True
        except ValueError:
            print("Incorrect date format: should be DD-MM-YYYY")
            return False


d = MyDate("10-12-2020")
print(d.extract_date_numbers("11-12-2020"))

s = MyDate.is_valid_date("19-10-2030")
print(s)