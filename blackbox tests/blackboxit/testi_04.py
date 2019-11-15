import os
while True:
	try:
		asiakkaat = int(input("Syötä asiakkaiden määrä, kokonaislukuna: "))
	except ValueError:
		print("Et syöttänyt kokonaislukua.")
	else:
		break

while True:
	try:
		marginaali = int(input("Syötä tuotantokustannus, kokonaislukuna: "))
	except ValueError:
		print("Et syöttänyt kokonaislukua.")
	else:
		break

rahat = []
index = range(asiakkaat)
for i in index:
    x = i + 1
    rahat.append(x)


markkina = []
y = asiakkaat

for h in rahat:
    n = h - 1
    x = y * rahat[n]
    markkina.append(x)
    y = asiakkaat - h
    if n > 0:
        if h > marginaali:
            kustannus = marginaali * y
            hinta = h
            voitto = markkina[n] - kustannus
            break

print("Sopiva markkinahinta on " + str(hinta) + "F fiktiivistä valuuttayksikköä.")
print("Josta kertyy " + str(voitto) + "F voittoa.")
os.system("python.exe ./testit.py pause")