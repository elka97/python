"""4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат."""


class Car:
	speed = 0.0
	color = "red"
	name = ""
	is_police = False

	def __init__(self, color, speed, name, is_police=False):
		self.color = color
		self.speed = speed
		self.name = name
		self.is_police = is_police

	def go(self):
		print(f"Go...")

	def stop(self):
		print(f"Stop...")

	def turn(self, direction):
		print(f"Turn to {direction}")

	def show_speed(self):
		print(f"Speed: {self.speed}")


class TownCar(Car):

	def __init__(self, color, speed):
		super().__init__(color, speed, "Town car")

	def show_speed(self):
		if self.speed > 60:
			print(f"Speed exceeded! {self.speed} km/h")
			return
		super().show_speed()


class SportCar(Car):

	def __init__(self, color, speed):
		super().__init__(color, speed, "Sport car")


class WorkCar(Car):

	def __init__(self, color, speed):
		super().__init__(color, speed, "Work car")

	def show_speed(self):
		if self.speed > 40:
			print(f"Speed exceeded! {self.speed} km/h")
			return
		super().show_speed()


class PoliceCar(Car):

	def __init__(self, color, speed):
		super().__init__(color, speed, "Police car", True)


town_car = TownCar("Red", 100)
print(f"{town_car.color} {town_car.name}")
town_car.go()
town_car.stop()
town_car.turn('left')
town_car.show_speed()

sport_car = SportCar("Blue", 300)
print(f"{sport_car.color} {sport_car.name}")
sport_car.go()
sport_car.stop()
sport_car.turn('right')
sport_car.show_speed()

work_car = WorkCar("Grey", 50)
print(f"{work_car.color} {work_car.name}")
work_car.go()
work_car.stop()
work_car.turn('east-west')
work_car.show_speed()

police_car = PoliceCar("white", 50)
print(f"{police_car.color} {police_car.name} is police={police_car.is_police}")
police_car.go()
police_car.stop()
police_car.turn('south')
police_car.show_speed()