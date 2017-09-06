#!/usr/sh
# -*- coding: utf-8 -*-

import os
import glob
import shutil


def deplcer_doc_a_traiter():
    """
    fonction servant a deplacer le doc a traiter
    :return: 
    """
    p = glob.glob('*/')[0]
    che = os.getcwd() + '/' + p
    # chemin_fihier_a_traiter = os.listdir(che)
    src = che
    dst = '/home/fourier_saint/PycharmProjects/traite'
    if not os.path.exists(che):
        shutil.move(src, dst)
    else:
        print('ce dossier existe deja !')