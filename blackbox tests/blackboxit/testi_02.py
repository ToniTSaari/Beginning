import os
while True:
	try:
		asiakkaat = int(input("Syötä asiakkaiden määrä, kokonaislukuna: "))
	except ValueError:
		print("Et syöttänyt kokonaislukua.")
	else:
		break

rahat = []
index = range(asiakkaat)
for i in index:
    x = i + 1
    rahat.append(x)

print("Markkinoilla on " + str(asiakkaat) + " asiakasta.")
print("Joilla on 1F-" + str(asiakkaat) + "F fiktiivistä valuuttayksikköä.")
print(rahat)
os.system("python.exe ./testit.py pause")