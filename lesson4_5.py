#5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

input_list = [el for el in range(100, 1002, 2)]
#input_list = [el for el in range(10, 20, 2)] for test
print(input_list)

multiple_all = reduce(lambda x, y: x*y,  input_list)

print(multiple_all)


