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
    
if marginaali < asiakkaat:
    rahat = []
    index = range(asiakkaat)
    for i in index:
        x = i + 1
        rahat.append(x)


    markkina = []
    voitto = []
    y = asiakkaat

    for h in rahat:
        n = h - 1
        x = y * rahat[n]
        markkina.append(x)
        y = asiakkaat - h
        kustannus = marginaali * y
        tulos = markkina[n] - kustannus
        voitto.append(tulos)
        if n > 0:
            m = n - 1
            if voitto[n] > voitto[m]:
                hinta = h
                tuotto = voitto[n]

    print("Sopiva markkinahinta on " + str(hinta) + "F fiktiivistä valuuttayksikköä.")
    print("Josta kertyy " + str(voitto) + "F voittoa.")
else:
    print("Tuotanto on kannattamatonta!")
os.system("python.exe ./testit.py pause")