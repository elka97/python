# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from sys import argv
import itertools as it

# D:\python\lesson4>python lesson4_6.py 3

end = 10
try:
	start = int(argv[1:][0])
	# a
	iterator = it.count(start)
	my_list = list(next(iterator) for _ in range(end))
	print(my_list)
	# b
	i = 0
	for el in it.cycle(my_list):
		if i > end:
			break
		print(el)
		i += 1
except ValueError:
	print(f"Input invalid")
	exit()
