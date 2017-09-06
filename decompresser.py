# -*- coding:utf-8 -*-
import zipfile
import os.path
import os


def dezip(filezip, pathdst=''):
    if pathdst == '': pathdst = os.getcwd()
    # on dezippe dans le repertoire locale
    zfile = zipfile.ZipFile(filezip, 'r')
    for i in zfile.namelist():
        # On parcourt l'ensemble des fichiers de l'archive
        print(i)
        if os.path.isdir(i):
            # S'il s'agit d'un repertoire, on se contente de creer le dossier
            try:
                os.makedirs(pathdst + os.sep + i)
            except:
                pass
        else:
            try:
                os.makedirs(pathdst + os.sep + os.path.dirname(i))
            except:
                pass
            data = zfile.read(i)
            # lecture du fichier compresse
            fp = open(pathdst + os.sep + i, "wb")
            # creation en local du nouveau fichier
            fp.write(data)
            # ajout des donnees du fichier compresse dans le fichier local
            fp.close()
    zfile.close()

if __name__ == '__main__':

    dezip('AFNET.zip', 'AVISO')