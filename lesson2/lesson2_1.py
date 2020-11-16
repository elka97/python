#1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [None, 42, "ku-ku", True, 83.65, b"asc", 42, {"red", "green", "blue", "red"}, ("red", "green", "blue", "red"), ["red", "green", "blue", "red"], {1: 1, 2: 2}]
print(type(my_list))

if my_list[0] is None:
	print("OK None")
if type(my_list[1]) is int:
	print("OK int")
if type(my_list[2]) is str:
	print("OK string")

for el in my_list:
	print(f"{el} is {type(el)}")