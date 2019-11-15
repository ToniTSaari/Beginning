import os
dir = os.getcwd()
juuri = os.path.abspath('..')

print(dir)
print(juuri)

print(["Tiedosto","Koko"])

for file in os.listdir(dir):
    content = [file] + [str(os.path.getsize(os.path.join(dir, file)))]
    print(content)

print()
print(["Tiedosto","Koko"])

for file in os.listdir(juuri):
    content = [file] + [str(os.path.getsize(os.path.join(juuri, file)))]
    print(content)
