from datetime import datetime

seconds = input("Enter a time in seconds:")

while not seconds.isdigit():
	seconds = input("Enter a time in seconds:")

tm = datetime.fromtimestamp(int(seconds)).strftime("%I:%M:%S")
print(f"{tm}")
