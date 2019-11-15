import decimal

e = float(0)
m = float(0)
c = float(299792458)

while True:
	try:
		m = float(input("Syötä massa numerona: "))
	except ValueError:
		print("Et syöttänyt numeroa.")
	else:
		break
		
e = m * c ** 2
e = round(e, 4)

print("Energia on: " + str(e))
