"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

my_list = [2, 3, 4, 5, 6, 8, 13, 21, 88, 12, -6]
print(my_list)

with open("task5_5.txt", "a") as writer:
	writer.truncate(0)
	writer.write(" ".join(str(el)for el in my_list))

with open("task5_5.txt", "r") as reader:
	lines = reader.read()
	sum_list = [float(el) for el in lines.split()]
	print(f"Sum: {sum(sum_list)}")