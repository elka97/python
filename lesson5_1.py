"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""


with open("task5_1.txt", "w") as out_f:
	data = input("Write something: ")
	while len(data) > 0:
		out_f.write(f"{data}\n")
		data = input("Write something: ")
	print("End of file")