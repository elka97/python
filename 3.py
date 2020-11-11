ask_num = "Enter a number n, please:"
n = input(f"{ask_num}")

while not n.isdigit():
	n = input(f"{ask_num}")

n = int(n)
nn = int(f"{n}{n}")
nnn = int(f"{n}{n}{n}")
print(f"{n} {nn} {nnn}")
print(f"Result={n+nn+nnn}")