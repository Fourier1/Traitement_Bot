#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob


def decomp():
    """
    decompression des dossiers
    :return: 
    """
    chemin = os.getcwd()
    do = glob.glob('*.zip')
    for doc in do:
        if doc in os.listdir(chemin):
            if doc in do:
                print(doc)
                os.system('unzip ' + doc)
                glob.glob(chemin)
#
#                 # shutil.move(dest, source)
# if __name__ == '__main__':
#     decomp()
