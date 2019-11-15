import os
while True:
    try:
        testi = int(input("Valitse funktio 2 - 10 tai syötä 0 lopettaaksesi: "))
        if testi > 1 and testi < 11:
            break
        elif testi == 0:
            while True:
                try:
                    kysy = str(input("Haluatko lopettaa [Y/N]"))
                except ValueError:
                    print("Et syöttänyt [Y/N].")
                else:
                    break
        if kysy == "Y" or kysy == "y":
            break
    except ValueError:
        print("Et syöttänyt integeriä.")

if testi == 2:
    os.system("python.exe ./blackboxit/testi_02.py pause")
elif testi == 3:
    os.system("python.exe ./blackboxit/testi_03.py pause")
elif testi == 4:
    os.system("python.exe ./blackboxit/testi_04.py pause")
elif testi == 5:
    os.system("python.exe ./blackboxit/testi_05.py pause")
elif testi == 6:
    os.system("python.exe ./blackboxit/testi_06.py pause")
elif testi == 7:
    os.system("python.exe ./blackboxit/testi_07.py pause")
elif testi == 8:
    os.system("python.exe ./blackboxit/testi_08.py pause")
elif testi == 9:
    os.system("python.exe ./blackboxit/testi_09.py pause")
elif testi == 10:
    os.system("python.exe ./blackboxit/testi_10.py pause")