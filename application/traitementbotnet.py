#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path

from application.config import ENTETES, ASN_OPERATEURS
from application.copierfichier import Copyafnet, Copyaviso, Copymoov, Copynsia, Copynvipnet, Copyyoomee

from application.creerdoc import dossiermoov, dossieraviso, dossierafnet, dossiernsia, dossiervipnet, dossieryoomee

listdoc = ['AVISO', 'AFNET', 'MOOV', 'NSIA', 'VIPNET', 'YOOMEE', 'DOC_COMP']


class TraiterfichierAVISO:
    """
    la classe de traitement des fichiers csv AVISO
    """
    def aviso(self):
        mypath = os.getcwd()
        for path, dirs, files in os.walk(mypath):
            for doc in listdoc:
                if doc in path:
                    print(doc)
                    continue
                    # for path, files in os.listdir(mypath):
                for filename in files:
                    # f = os.path.join(path, filename)
                    # print(path)
                    if os.path.isfile(filename) and filename.endswith('.csv'):
                        entetes = ENTETES
                        contenu = ''
                        # element = 'tester.csv'
                        sourc = open(filename, 'r')
                        result = os.path.splitext(filename)[0] + '_AVISO.csv'
                        entete = ";".join(entetes) + "\n"
                        for ligne in sourc:
                            if ASN_OPERATEURS[0] in ligne:
                                contenu += ligne
                                sourc = open(result, 'w')
                                sourc.write(entete)
                                sourc.write(contenu)
                                sourc.close()
                                dossieraviso()
                                Copyaviso()

                            else:
                                pass


class TraiterfichierAFNET:
    """
    la classe de traitement des fichiers csv AFNET
    """
    def afnet(self):
        mypath = os.getcwd()
        for path, dirs, files in os.walk(mypath):
            for doc in listdoc:
                if doc in mypath:
                    print(doc)
                    continue
                # for path, files in os.listdir(mypath):
                for filename in files:
                    # f = os.path.join(path, filename)
                    # print(path)
                    if os.path.isfile(filename) and filename.endswith('.csv'):
                        entetes = ENTETES
                        # valeur = ASN_OPERATEURS
                        contenu = ''
                        # element = 'tester.csv'
                        sourc = open(filename, 'r')
                        result = os.path.splitext(filename)[0] + '_AFNET.csv'
                        entete = ";".join(entetes) + "\n"
                        for ligne in sourc:
                            if ASN_OPERATEURS[1] in ligne:
                                contenu += ligne
                                sourc = open(result, 'w')
                                sourc.write(entete)
                                sourc.write(contenu)
                                sourc.close()
                                dossierafnet()
                                Copyafnet()

                            else:
                                pass


class TraiterfichierMOOVCI:
    """
    la classe de traitement des fichiers csv MOOV-CI
    """
    def moov(self):
        mypath = os.getcwd()
        for path, dirs, files in os.walk(mypath):
            for doc in listdoc:
                if doc in mypath:
                    print(doc)
                    continue
                # for path, files in os.listdir(mypath):
                for filename in files:
                    # f = os.path.join(path, filename)
                    # print(path)
                    if os.path.isfile(filename) and filename.endswith('.csv'):
                        entetes = ENTETES
                        # valeur = ASN_OPERATEURS
                        contenu = ''
                        # element = 'tester.csv'
                        sourc = open(filename, 'r')
                        result = os.path.splitext(filename)[0] + '_MOOV-CI.csv'
                        entete = ";".join(entetes) + "\n"
                        for ligne in sourc:
                            if ASN_OPERATEURS[2] in ligne:
                                contenu += ligne
                                sourc = open(result, 'w')
                                sourc.write(entete)
                                sourc.write(contenu)
                                sourc.close()
                                dossiermoov()
                                Copymoov()

                            else:
                                pass


class TraiterfichierNSIACI:
    """
    la classe de traitement des fichiers csv NSIA-CI
    """
    def nsia(self):
        mypath = os.getcwd()
        for path, dirs, files in os.walk(mypath):
            for doc in listdoc:
                if doc in mypath:
                    print(doc)
                    continue
                # for path, files in os.listdir(mypath):
                for filename in files:
                    # f = os.path.join(path, filename)
                    # print(path)
                    if os.path.isfile(filename) and filename.endswith('.csv'):
                        entetes = ENTETES
                        # valeur = ASN_OPERATEURS
                        contenu = ''
                        # element = 'tester.csv'
                        sourc = open(filename, 'r')
                        result = os.path.splitext(filename)[0] + '_NSIA-CI.csv'
                        entete = ";".join(entetes) + "\n"
                        for ligne in sourc:
                            if ASN_OPERATEURS[3] in ligne:
                                contenu += ligne
                                sourc = open(result, 'w')
                                sourc.write(entete)
                                sourc.write(contenu)
                                sourc.close()
                                dossiernsia()
                                Copynsia()

                            else:
                                pass


class TraiterfichierVIPNET:
    """
    la classe de traitement des fichiers csv VIPNET-CT
    """
    def vipnet(self):
        mypath = os.getcwd()
        for path, dirs, files in os.walk(mypath):
            for doc in listdoc:
                if doc in mypath:
                    print(doc)
                    continue

                # for path, files in os.listdir(mypath):
                for filename in files:
                    # f = os.path.join(path, filename)
                    # print(path)
                    if os.path.isfile(filename) and filename.endswith('.csv'):
                        entetes = ENTETES
                        # entetes = str(entetes)
                        # valeur = ASN_OPERATEURS
                        contenu = ''
                        # element = 'tester.csv'
                        sourc = open(filename, 'r')
                        result = os.path.splitext(filename)[0] + '_VIPNET.csv'
                        entete = ";".join(entetes) + "\n"
                        for ligne in sourc:
                            if ASN_OPERATEURS[4] in ligne:
                                contenu += ligne
                                sourc = open(result, 'w')
                                sourc.write(entete)
                                sourc.write(contenu)
                                sourc.close()
                                dossiervipnet()
                                Copynvipnet()

                            else:
                                pass


class TraiterfichierYOOMEE:
    """
    la classe de traitement des fichiers csv YOOMEE
    """
    def yoomee(self):
        mypath = os.getcwd()
        for path, dirs, files in os.walk(mypath):
            for doc in listdoc:
                if doc in mypath:
                    print(doc)
                    continue

                # for path, files in os.listdir(mypath):
                for filename in files:
                    # f = os.path.join(path, filename)
                    # print(path)
                    if os.path.isfile(filename) and filename.endswith('.csv'):
                        entetes = ENTETES
                        # entetes = str(entetes)
                        # valeur = ASN_OPERATEURS
                        contenu = ''
                        # element = 'tester.csv'
                        sourc = open(filename, 'r')
                        result = os.path.splitext(filename)[0] + '_YOOMEE.csv'
                        entete = ";".join(entetes) + "\n"
                        for ligne in sourc:
                            if ASN_OPERATEURS[5] in ligne:
                                contenu += ligne
                                sourc = open(result, 'w')
                                sourc.write(entete)
                                sourc.write(contenu)
                                sourc.close()
                                dossieryoomee()
                                Copyyoomee()

                            else:
                                pass
#
# if __name__ == '__main__':
#
#     aviso = TraiterfichierAVISO.aviso(None)
#     afnet = TraiterfichierAFNET.afnet(None)
#     moov = TraiterfichierMOOVCI.moov(None)
#     nsia = TraiterfichierNSIACI.nsia(None)
#     vipnet = TraiterfichierVIPNET.vipnet(None)
#     yoomee = TraiterfichierYOOMEE.yoomee(None)