#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os.path
import shutil

globals()
cheminfichier = os.getcwd()


def Copyaviso():
    """
    copier les fichiers aviso en fonction de leurs nom et les placer 
    dans les dossiers respectivent
    :return: 
    """

    if os.path.exists(cheminfichier):
        for fichier in glob.glob(cheminfichier + '/*_AVISO.csv'):
            copyfile = os.path.basename(fichier)
            shutil.move(fichier, cheminfichier +'/AVISO/' + copyfile)


def Copyafnet():
    """
    copier les fichiers afnet en fonction de leurs nom et les placer 
    dans les dossiers respectivent
    :return: 
    """

    if os.path.exists(cheminfichier):
        for fichier in glob.glob(cheminfichier + '/*_AFNET.csv'):
            copyfile = os.path.basename(fichier)
            shutil.move(fichier, cheminfichier + '/AFNET/' + copyfile)


def Copymoov():
    """
    copier les fichiers moov en fonction de leurs nom et les placer 
    dans les dossiers respectivent
    :return: 
    """

    if os.path.exists(cheminfichier):
        for fichier in glob.glob(cheminfichier + '/*_MOOV-CI.csv'):
            copyfile = os.path.basename(fichier)
            shutil.move(fichier, cheminfichier + '/MOOV/' + copyfile)


def Copynsia():
    """
    copier les fichiers moov en fonction de leurs nom et les placer 
    dans les dossiers respectivent
    :return: 
    """

    if os.path.exists(cheminfichier):
        for fichier in glob.glob(cheminfichier + '/*_NSIA-CI.csv'):
            copyfile = os.path.basename(fichier)
            shutil.move(fichier, cheminfichier + '/NSIA/' + copyfile)


def Copynvipnet():
    """
    copier les fichiers moov en fonction de leurs nom et les placer 
    dans les dossiers respectivent
    :return: 
    """

    if os.path.exists(cheminfichier):
        for fichier in glob.glob(cheminfichier + '/*_VIPNET.csv'):
            copyfile = os.path.basename(fichier)
            shutil.move(fichier, cheminfichier + '/VIPNET/' + copyfile)


def Copyyoomee():
    """
    copier les fichiers moov en fonction de leurs nom et les placer 
    dans les dossiers respectivent
    :return: 
    """

    if os.path.exists(cheminfichier):
        for fichier in glob.glob(cheminfichier + '/*_YOOMEE.csv'):
            copyfile = os.path.basename(fichier)
            shutil.move(fichier, cheminfichier + '/YOOMEE/' + copyfile)
#
# if __name__ == '__main__':
#     Copyaviso()
#     Copyafnet()
