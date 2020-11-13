num_str = input("Enter a long round number:")

while not num_str.isdigit():
	num_str = input("Enter a long round number:")

length = len(num_str)
print(f"{num_str} {length}")
arr = tuple(num_str)
result = 0
temp = 0
count = 0
while length > count:
	temp = int(arr[count])
	#print(f"{temp}")
	if temp > result:
		result = temp
		count += 1

print(f"Max digit in {num_str} is {result}")
