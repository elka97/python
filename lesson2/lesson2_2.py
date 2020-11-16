# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input()

input_list = list(input("Please, enter several entries: ").split())
count = len(input_list)

if count > 2:
	print(input_list)
	for i, el in enumerate(input_list):
		if i % 2 == 0 and i < count-1:
			input_list[i+1], input_list[i] = input_list[i:i+2]
	print(input_list)
else:
	print("The list too small")