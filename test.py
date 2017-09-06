#!/usr/sh
# -*- coding: utf-8 -*-

import os
import glob


ch = os.getcwd()
d = glob.glob('*.zip')
print(d)
for doc in ch:
    if doc in os.listdir(ch):
        if doc in d:
            # print(doc)
            os.system('unzip ' + doc)
            print("s")

# listdoc = ['AVISO.zip', 'AFNET.zip', 'MOOV.zip', 'NSIAzip', 'VIPNET.zip', 'YOOMEE.zip']
#
# ch = os.getcwd() + '/DOC_COMP'
# for doc in listdoc:
#     if doc in os.listdir(ch):
#         if doc == 'AVISO.zip':
#             print(doc)

# ret = os.system('cd ../' + os.path.basename(os.getcwd()))
# source = '/home/fourier_saint/PycharmProjects/traite/application/DOC_COMP'
# dest = '/home/fourier_saint/PycharmProjects/traite/DOC_COMP'
# shutil.move(dest, source)
# shutil.copy(dest, source)
# chemin = os.getcwd()
# listdoc = ['AVISO', 'AFNET', 'MOOV', 'NSIA', 'VIPNET', 'YOOMEE']
# do = glob.glob('*/')
# for doc in listdoc:
#     if doc in os.listdir(chemin):
#         if doc in listdoc:
#             print(doc)
#             cmd = 'zip -r ' + doc + '.zip ' + doc
#             print(cmd)
#             os.system(cmd)

            # os.system('zip -r docc, doc')
            # zipdirectory(doc + '.zip', doc)