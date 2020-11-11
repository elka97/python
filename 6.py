a = 5
b = 10
step = 0.1
count = 1

print(f"day {count}: {a}")
while a <= b:
	a = round((a*step+a), 2)
	count += 1
	print(f"day {count}: {a}")

print(f"Ответ: на {count}-й день спортсмен достиг результата — не менее {a} км")