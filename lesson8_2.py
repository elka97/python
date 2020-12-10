"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой."""


class ZeroDivisionException(Exception):
    def __init__(self, a, b):
        self.message = f"Can't divide on zero {a}/{b}"


x, y = map(int, input("Enter 2 numbers:").split())

try:
    if y == 0:
        raise ZeroDivisionException(x, y)
    print(x / y)
except ZeroDivisionError:
    print("Standard error ZeroDivisionError")
except ZeroDivisionException as err:
    print(err.message)