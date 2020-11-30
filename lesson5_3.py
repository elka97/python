"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

workers = 0
with open("task3.txt", "r") as f:
	lines = f.readlines()
	workers += len(lines)
	my_list = [el.split() for el in lines]
	small_salary = [el for el, el1 in my_list if float(el1) < 20000.00]
	print(f"Oклад менее 20 тыс.: {small_salary}")
	salary_total = [float(el1) for el, el1 in my_list]
	print(f"Average salary: {sum(salary_total)/workers}")