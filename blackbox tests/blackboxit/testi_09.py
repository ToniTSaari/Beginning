import os
while True:
	try:
		asiakkaat = int(input("Syötä asiakkaiden määrä, kokonaislukuna: "))
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
        m = n - 1
        if markkina[n] > markkina[m]:
            hinta = h
            voitto = markkina[n]

taxes = int(voitto * alv)

if alv != 0:
    print("Arvonlisäveroa kertyy yhteensä " + str(taxes) + "F")
else:
    print("Verovapaasta tavarasta harvoin kertyy veroja, eikös?")
os.system("python.exe ./testit.py pause")