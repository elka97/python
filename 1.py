#---------------1-------------------
x = 10
a = "ku ku"
y = 10.88
print(f"{x} {a} {y}")

ask_num = "Enter a number n, please:"
n = input(f"{ask_num}")

if n.isdigit():
	print(f"{n}")
else:
	n = input(f"{ask_num}")

ask_string = "Write something:"
inp_str = input(f"{ask_string}")
print(f"{inp_str}")