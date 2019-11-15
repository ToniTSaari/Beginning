spam = str(".")
while True:
	try:
		spam = str(input("Syötä sikanautaa(tekstinä ja englanniksi): "))
	except ValueError:
		print("Et syöttänyt tekstinä.")
	else:
		break

if spam == "spam" or spam == "Spam" or spam == "Sikanauta" or spam == "sikanauta":
    if spam == "Sikanauta":
        print("Bloody Vikings!")
    else:
        print("Lovely spam! Wonderful spam!")
else:
    print("I don't want ANY spam!")
