spam = int(0)
while True:
	try:
		spam = int(input("Syötä määrä integerinä: "))
	except ValueError:
		print("Et syöttänyt integeriä.")
	else:
		break
spamming = range(spam)
for x in spamming:
    if x == 2:
        print("Eggs")
    elif x == 4:
        print("Bacon")
    elif x == 7:
        print("Sausage")
    elif x == 11:
        print("Tomato")
    elif x == 16:
        print("Baked beans")
    else:
        print("Spam")
