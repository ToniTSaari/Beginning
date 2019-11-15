import os
juuri = os.path.abspath('.')


for root, dirs, files in os.walk(juuri):
    for dir in dirs:
        for file in files:
            koko = str(os.path.getsize(os.path.join(root, file))) + " KB"
            content = os.path.join(root, file) + " " + koko
            print(content)
