"""4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь."""
from abc import ABC, abstractmethod
from datetime import datetime
import enum


class CheckQuantityError(Exception):
    def __init__(self, param, message):
        super(CheckQuantityError, self).__init__(f"{message}, but {param} sent")


class Departments(enum.Enum):
    IT = 1
    Accounting = 2
    Management = 3
    Product = 4
    Marketing = 5


class Warehouse:
    units = {}

    def __init__(self):
        self.units = {}

    def info(self):
        print(f"{datetime.today()}: Warehouse state: {self.units}")

    def add_equipment(self, equipment, quantity):
        if not isinstance(equipment, OfficeEquipment):
            print(f"Error: not a valid OfficeEquipment")
            return
        try:
            if int(quantity) <= 0:
                raise CheckQuantityError(quantity, "Expecting a positive number")
            if equipment.eq_type in self.units:
                self.units[equipment.eq_type] += int(quantity)
            else:
                self.units[equipment.eq_type] = int(quantity)
            print(f"{datetime.today()}: Stored {quantity} {equipment.eq_type}s.")
            self.info()
        except CheckQuantityError as invalid_ex:
            print(f"{invalid_ex}")
        except ValueError as ex:
            print(f"Error: Quantity of {equipment.eq_type} should be a number, but '{quantity}' entered: {ex}")
        except Exception as ex1:
            print(f"{ex1}")
            raise

    def assign_to_department(self, equipment, quantity, department):
        if not isinstance(equipment, OfficeEquipment):
            print(f"Error: not a valid OfficeEquipment")
            return
        try:
            if int(quantity) <= 0:
                raise CheckQuantityError(quantity, "Expecting a positive number")
            if not equipment.eq_type in self.units:
                print(f"No {equipment.eq_type}s found.")
                return
            if self.units[equipment.eq_type] < int(quantity):
                print(f"Not enough {equipment.eq_type}s found.")
                return
            self.units[equipment.eq_type] -= int(quantity)
            print(f"{datetime.today()}: Moved {quantity} {equipment.eq_type}s to {department} dept.")
            self.info()
        except CheckQuantityError as invalid_ex:
            print(f"{invalid_ex}")
        except ValueError as ex:
            print(f"Error: Quantity of {equipment.eq_type} should be a number, but '{quantity}' entered: {ex}")
        except Exception as ex1:
            print(f"{ex1}")
            raise


class OfficeEquipment(ABC):
    def __init__(self, eq_type, name, producer, production_year):
        self.eq_type = eq_type
        self.name = name
        self.producer = producer
        self.production_year = production_year

    @abstractmethod
    def info(self):
        return f"OfficeEquipment: {self.eq_type} '{self.name}' production:{self.producer} {self.production_year}"


class Printer(OfficeEquipment):
    def __init__(self, name, producer, production_year, laser, speed):
        super().__init__("Printer", name, producer, production_year)
        self.laser = laser
        self.speed = speed

    def info(self):
        common_info = super().info()
        print(f"{common_info} Laser:{self.laser} Speed:{self.speed}")


class Scanner(OfficeEquipment):
    def __init__(self, name, producer, production_year, three_d):
        super().__init__("Scanner", name, producer, production_year)
        self.three_d = three_d

    def info(self):
        common_info = super().info()
        print(f"{common_info} 3d:{self.three_d}")


printer1 = Printer("2020", "HP", 2018, True, 300)
printer2 = Printer("123", "Samsung", 2019, False, 250)
printer1.info()
printer2.info()

scanner1 = Scanner("878", "Samsung", 2020, True)
scanner2 = Scanner("454545", "Lenovo", 2021, True)
scanner1.info()
scanner2.info()

"""6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП."""

print("\t\tPopulate warehouse")
storage = Warehouse()
storage.add_equipment(printer1, 4)
storage.add_equipment(printer1, "a")
storage.add_equipment(printer2, 2)
storage.add_equipment(scanner1, 3)
storage.add_equipment(scanner2, -1)
storage.add_equipment(scanner2, 18)

print("\t\tMove from warehouse to some department")
storage.assign_to_department(printer1, 2, Departments.Accounting)
storage.assign_to_department(printer1, "xx", Departments.Management)
storage.assign_to_department(printer2, 2, Departments.IT)
storage.assign_to_department(scanner1, 3, Departments.Accounting)
storage.assign_to_department(scanner2, -7, Departments.Marketing)
storage.assign_to_department(scanner2, 18, Departments.Product)
storage.assign_to_department(scanner2, 18, Departments.Product)
