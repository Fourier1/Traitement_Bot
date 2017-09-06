#!/usr/bin/env python
# -*- coding: utf-8 -*-

import zipfile
import os.path
import glob


def zipdirectory(filezip, pathzip):
    lenpathparent = len(pathzip) + 1
    # utile si on veut stocker les chemins relatifs

    def _zipdirectory(zfile, path):
        for i in glob.glob(path + '\\*'):
            if os.path.isdir(i):
               _zipdirectory(zfile, i)
            else:
                print(i)
                zfile.write(i, i[lenpathparent:])
                # zfile.write(i) pour stocker les chemins complets

    zfile = zipfile.ZipFile(filezip, 'w', compression=zipfile.ZIP_DEFLATED)
    _zipdirectory(zfile, pathzip)
    zfile.close()

if __name__ == '__main__':

   zipdirectory('/home/fourier_saint/PycharmProjects/traite/AVISO.zip', 'AVISO')
#    zipdirectory('AFNET.zip', 'AFNET')
#     zipdirectory('NSIA.zip', 'NSIA')
#     zipdirectory('MOOV.zip', 'MOOV')
#     zipdirectory('VIPNET.zip', 'VIPNET')
#     zipdirectory('YOOMEE.zip', 'YOOMEE')
#
