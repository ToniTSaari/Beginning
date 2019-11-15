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

while True:
	try:
		marginaali = int(input("Syötä tuotantokustannus, kokonaislukuna: "))
	except ValueError:
		print("Et syöttänyt kokonaislukua.")
	else:
		break

rahat = []
if asiakkaat > kilpailu:
    if kilpailu != 0:
        kilpailu = kilpailu + 1
        asiakkaat = int(asiakkaat / kilpailu)
        osuus = int(100 / kilpailu)
    else:
        osuus = 100
    index = range(asiakkaat)
    for i in index:
        x = i + 1
        rahat.append(x)

    markkina = []
    voitto = []
    y = asiakkaat
    tuottavuus = False

    for h in rahat:
        n = h - 1
        x = y * rahat[n]
        markkina.append(x)
        y = asiakkaat - h
        kustannus = marginaali * y
        tulos = markkina[n] - kustannus
        if tulos > 0:
            voitto.append(tulos)
            if n > 0:
                m = n - 1
                if voitto[n] > voitto[m]:
                    hinta = h
                    tuotto = voitto[n]
                    tuottavuus = True

    if tuottavuus == True:
        print("Markkinaosuus on " + str(osuus) + "%")
        print("Sopiva markkinahinta on " + str(hinta) + "F fiktiivistä valuuttayksikköä.")
        print("Josta kertyy " + str(tuotto) + "F voittoa.")
    else:
        print("Tuotanto ei ole kannattavaa!")
else:
    print("Markkinat ovat kyllästyneet!")
os.system("python.exe ./testit.py pause")