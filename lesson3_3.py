# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(v1, v2, v3):
	my_list = [v1, v2, v3]
	max1 = max(my_list)
	my_list.remove(max1)
	max2 = max(my_list)
	return max1 + max2


result = my_func(37, -14, 5)
print(result)
