#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
#Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(name, last_name, year_birth, city, email, phone):
	data = f"{name} {last_name}, born in {year_birth}. City: {city} email: {email} phone: {phone}"
	return data


user_info = user_data(name="Vasya", last_name="Pupkin", year_birth=1878, city="NY", email="ss@com", phone="123-456")
print(user_info)
