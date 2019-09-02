fizz = int(0)
buzz = int(0)
total = int(0)
while True:
	try:
		fizz = int(input("Enter Fizz as int: "))
		buzz = int(input("Enter Buzz as int: "))
		total = int(input("Enter FizzBuzz sequence: "))
	except ValueError:
		print("You didn't enter an integer, starting from the top.")
	else:
		break
for i in range(total):
    message = ""
    if i % fizz == 0 | i % buzz == 0:
        message = "FizzBuzz"
    elif i % fizz == 0:
        message = "Fizz"
    elif i % buzz == 0:
        message = "Buzz"
    else:
        message = str(i)
    print(message)
