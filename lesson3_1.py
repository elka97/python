# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divide(var1, var2):
	if var2 == 0:
		return 0
	return var1 / var2

var_1 = input("Enter the first number: ")
while not var_1.isnumeric():
	var_1 = input("Enter the first number: ")

var_1 = float(var_1)

var_2 = input("Enter the second number: ")
while not var_2.isnumeric():
	var_2 = input("Enter the second number: ")

var_2 = float(var_2)
print(f"{var_1} {var_2}")

print(f"result={divide(var_1, var_2)}")
