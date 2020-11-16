# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

commodity_dict = {"name": "", "price": 0, "amount": 0, "units": 0}
commodities_list = [(0, {'name': 'aaa', 'price': '11', 'amount': '1', 'units': '1'}), (1, {'name': 'bbb', 'price': '22', 'amount': '2', 'units': '2'})]

names = []
prices = []
amounts = []
units = []



commodities_list = []

for i in range(2):
	commodity_dict = {k: [] for k in commodity_dict}
	name = input("Enter a name: ")
	while len(name) < 0:
		name = input("Enter a name:")
	commodity_dict["name"] = name

	price = input("Enter a price: ")
	while not price.isdigit() or int(price) < 0:
		price = input("Enter a price:")
	commodity_dict["price"] = price

	amount = input("Enter a amount: ")
	while not amount.isdigit() or int(amount) < 0:
		amount = input("Enter a amount:")
	commodity_dict["amount"] = amount

	unit = input("Enter a unit: ")
	while len(unit) < 0:
		unit = input("Enter a unit:")
	commodity_dict["units"] = unit

	commodities_list.append((i, commodity_dict))

print(f"Commodities list: {commodities_list}")

# clear
commodity_dict = {k: [] for k in commodity_dict}

names = []
prices = []
amounts = []
units = []

for el in commodities_list:
	values = list(el[1].values())
	keys = list(el[1].keys())
	#print(f"=={values} {keys}")

	names.append(values[0])
	commodity_dict[keys[0]] = names

	prices.append(values[1])
	commodity_dict[keys[1]] = prices

	amounts.append(values[2])
	commodity_dict[keys[2]] = amounts

	units.append(values[3])
	commodity_dict[keys[3]] = units

print(f"Analytics: {commodity_dict}")
