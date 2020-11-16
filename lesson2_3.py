#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

months_list = [12]
months_list.extend(range(1, 12))
months_dict = {"winter": (12, 1, 2), "spring": (3, 4, 5), "summer": (6, 7, 8), "autumn": (9, 10, 11)}
#print(months_list)
# print(months_dict)

month = input("Enter a month 1-12: ")
while not month.isdigit() or int(month) <= 0 or int(month) > 12:
	month = input("Enter a month 1-12:")

month = int(month)

# dictionary
for k, val in months_dict.items():
	if month in val:
		print(f"Month {month} of {k}")

# list
if month in months_list[0:3]:
	print(f"Month {month} of winter")
elif month in months_list[3:6]:
	print(f"Month {month} of spring")
elif month in months_list[6:9]:
	print(f"Month {month} of summer")
elif month in months_list[9:12]:
	print(f"Month {month} of autumn")










