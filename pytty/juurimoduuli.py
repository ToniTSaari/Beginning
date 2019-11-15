import os, zipfile, shutil, ftputil, tempfile
from time import gmtime, strftime
from backday import backday
from pathlib import Path

if os.path.exists('c:/tmep')!=True:

    os.mkdir('c:/tmep')

juuri = os.getcwd()
nimi = backday()
kohde = Path('c:/tmep/' + nimi)
temppi = tempfile.mkdtemp()
zippi = os.path.join(kohde, strftime('%H%m', gmtime())) + ".zip"

def juurimod():
    if os.path.exists(zippi):

        os.remove(zippi)
        
    valmis = "Varmuuskopiointi valmis!" + "\n"
    f = open('c:/tmep/halko.txt', 'a')
    if os.path.exists(kohde)!=True:

        os.mkdir(kohde)
        f.write("Luotiin kansio" + "\n")
        valmis += " Luotiin kansio" + "\n"

    f.write("\nKopsattu " + strftime('%d.%m.%Y %H:%m', gmtime()) + "\n")
    zf = zipfile.ZipFile(zippi, "a", zipfile.ZIP_DEFLATED)

    with ftputil.FTPHost('164.215.36.22', 'ohjelmointimm19', 'HD5a6s7d8ssaB') as host:

        names = host.listdir(host.curdir)
        print(names)
        for name in names:

            print(name)
            if host.path.isfile(name):

                os.chdir(temppi)
                host.download(name, name)
                zf.write(os.path.join(temppi, name))
                valmis += " Haettiin tiedosto " + name + " palvelimelta" + "\n"

    for root, dirs, files in os.walk(juuri):

        for file in files:

            koko = str(os.path.getsize(os.path.join(root, file))) + " KB"
            content = os.path.join(root, file) + " " + koko
            print(content)
            f.write(os.path.join(root, file) + ' ' + koko + '\n')
            zf.write(os.path.join(root, file))
            valmis += " kopioitiin tiedosto " + file + "\n"

    zf.close()
    f.close()
    return valmis