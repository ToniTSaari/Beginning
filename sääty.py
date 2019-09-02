class Spam:
    def __init__(eggs, bacon):
        eggs.bacon = bacon
    def numbers(sausage):
        spamming = range(sausage.bacon)
        for x in spamming:
            if x == 2:
                print("Eggs")
            elif x == 4:
                print("Bacon")
            elif x == 7:
                print("Sausage")
            elif x == 11:
                print("Tomato")
            elif x == 16:
                print("Baked beans")
            else:
                print("Spam")
    def words(ham):
        if ham.bacon == "spam" or ham.bacon == "Spam" or ham.bacon == "Sikanauta" or ham.bacon == "sikanauta":
            if ham.bacon == "Sikanauta" or ham.bacon == "sikanauta":
                print("Bloody Vikings!")
            else:
                print("Lovely spam! Wonderful spam!")
        else:
            print("I don't want ANY spam!")

try:
    incoming = input("Syötä spam: ")
    spam = int(incoming)
except ValueError:
    spam = incoming

s = Spam(spam)

if type(spam) is int:
    s.numbers()
else:
    s.words()
