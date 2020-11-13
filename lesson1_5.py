earnings_str = input("Enter a profit:")
costs_str = input("Enter a costs:")

while not earnings_str.isnumeric():
	earnings_str = input("Enter a profit:")

while not costs_str.isnumeric():
	costs_str = input("Enter a costs:")

earnings = float(earnings_str)
costs = float(costs_str)

if earnings > costs:
	print("You got a profit!")
	print(f"Profitability: {earnings / costs}")

	emp_str = input("Enter an employees number:")

	if emp_str.isdigit():
		print(f"Profit per employee: {earnings / int(emp_str)}")
	else:
		print("employees is not a number")
else:
	print("No profit so far(-:")

