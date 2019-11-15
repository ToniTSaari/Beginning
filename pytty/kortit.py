import random
maat = ["Pata", "Ruutu", "Hertta", "Risti"]
arvot = ["Ässä"]
arvot = arvot + [str(x) for x in range(2,10)]
arvot = arvot + ["Jätkä","Rouva","Kunkku"]
kortit = [x + " - " + y for x in maat for y in arvot]
random.shuffle(kortit)
print("Kortteja on ", len(kortit))
print("Viisi satunnaista korttia: ")
for kortti in kortit[0:5]:
    print(kortti)
    