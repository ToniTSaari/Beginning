x = input("Anna arvo: ")
y = input("Anna toinen arvo: ")
try:
    val1 = int(x) # varmistetaan, että x on int
    val2 = int(y) # varmistetaan, että y on int
    tulo = val1 * val2
    yht = val1+val2
    print("\nTulo",tulo, "\nYhteensä",yht )
except ValueError: # annetut luvut eivät ole kokonaislukuja
    print("Anna arvoiksi kokonaislukuja")
    print("Ä"+"l"+"ä","h"+"u"+"i"+"j"+"a"+"a")
       
