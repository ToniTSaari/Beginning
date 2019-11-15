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

print("1# ALV 24%\n2# ALV 14%\n3# ALV 10%\n4# ALV 0%")

while True:
    try:
        alvLuokka = int(input("Valitse arvonlisäluokka: "))
        if alvLuokka > 0 and alvLuokka < 5:
            break
    except ValueError:
        print("Et syöttänyt integeriä.")

if alvLuokka == 1:
    alv = 0.24
elif alvLuokka == 2:
    alv = 0.14
elif alvLuokka == 3:
    alv = 0.10
else:
    alv = 0

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
        voitto.append(tulos)
        if alv > 0:
            vero = int(tulos * alv)
            tulos = tulos - vero
        if tulos > 0:
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