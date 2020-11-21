# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

#D:\python\lesson4>python lesson4_1.py 12 0.56 233

def calc_salary(hours, h_salary, bonus):
	return float(hours) * float(h_salary) + float(bonus)


try:
	hr, h_s, bon = argv[1:]
	print(f"Hours:{hr} Salary per hour: {h_s} Bonus: {bon} => Total: {calc_salary(hr, h_s, bon)}")
except ValueError:
	if len(argv) < 5:
		print(f"Missing params or Input invalid: need 3 numeric params")
		exit()
