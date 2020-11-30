"""Создать (не программно) текстовый файл со следующим содержимым:.
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
result = []

with open("task4.txt", "r", encoding="utf-8") as reader:
	for line in reader:
		words = line.split()
		eng = words
		eng[0] = my_dict.get(eng[0])
		eng_line = ' '.join([str(el) for el in eng])
		result.append(eng_line)


new_lines = "\n".join([str(el) for el in result])
with open("task4ru.txt", "w", encoding="utf-8") as writer:
	writer.write(str(new_lines))