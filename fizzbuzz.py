for i in range(101):
    message = ""
    if i % 3 == 0 | i % 5 == 0:
        message = "FizzBuzz"
    elif i % 3 == 0:
        message = "Fizz"
    elif i % 5 == 0:
        message = "Buzz"
    else:
        message = str(i)
    print(message)
