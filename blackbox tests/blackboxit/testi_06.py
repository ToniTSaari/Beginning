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
		kilpailu = int(input("Syötä kilpailevat tuotteet, kokonaislukuna: "))
	except ValueError:
		print("Et syöttänyt kokonaislukua.")
	else:
		break

rahat = []
if kilpailu != 0:
    kilpailu = kilpailu + 1
    asiakkaat = int(asiakkaat / kilpailu)
    osuus = int(100 / kilpailu)
index = range(asiakkaat)
for i in index:
    x = i + 1
    rahat.append(x)


markkina = []
y = asiakkaat

if asiakkaat > kilpailu:
    for h in rahat:
        n = h - 1
        x = y * rahat[n]
        markkina.append(x)
        y = asiakkaat - h
        if n > 0:
            m = n - 1
            if markkina[n] > markkina[m]:
                hinta = h
                tuotto = markkina[n]

        print("Markkinaosuus on " + str(osuus) + "%")
        print("Sopiva markkinahinta on " + str(hinta) + "F fiktiivistä valuuttayksikköä.")
        print("Josta kertyy " + str(tuotto) + "F voittoa.")
else:
    print("Markkinat ovat kyllästyneet!")
os.system("python.exe ./testit.py pause")