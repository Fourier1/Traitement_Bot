#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def Compress():
    """
    compression des fichiers
    :return: 
    """
    listdoc = ['AVISO', 'AFNET', 'MOOV', 'NSIA', 'VIPNET', 'YOOMEE']
    chemin = os.getcwd()
    # do = glob.glob('*/')
    for doc in listdoc:
        if doc in os.listdir(chemin):
            if doc in listdoc:
                # print(doc)
                cmd = 'zip -r ' + doc + '.zip ' + doc
                print(cmd)
                os.system(cmd)

