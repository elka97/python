"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров)."""


class Worker:
	name = ""
	surname = ""
	position = ""
	_income = {"wage": 0.0, "bonus": 0.0}

	def __init__(self, name, surname, position):
		self.name = name
		self.surname = surname
		self.position = position

	def set_income(self, wage, bonus):
		self._income["wage"] = wage
		self._income["bonus"] = bonus


class Position(Worker):

	def __init__(self, name, surname, position):
		super().__init__(name, surname, position)

	def get_full_name(self):
		return f"{self.name} {self.surname}"

	def get_total_income(self, wage, bonus):
		super().set_income(wage, bonus)
		return self._income


position = Position("Ivan", "Ivanov", "manager")
print(f"{position.get_full_name()}")
print(f"{position.get_total_income(55000.0, 20000.0)}")
