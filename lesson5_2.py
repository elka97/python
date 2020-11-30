"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке."""

with open("out_file.txt", "r") as out_f:
	my_list = out_f.readlines()
	print(f"Total lines:{len(my_list)}")
	for el in my_list:
		print(f"{el} {len(el.split())} words")