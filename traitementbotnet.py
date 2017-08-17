#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
from config import ENTETES, ASN_OPERATEURS
from creerdoc import dossiermoov, dossieraviso, dossierafnet, dossiernsia, dossiervipnet, dossieryoomee


class TraiterfichierAVISO:
    """
    la classe de traitement des fichiers csv AVISO 
    """
    entetes = ENTETES
    valeur = ASN_OPERATEURS
    contenu = ''
    element = 'tester.csv'
    sourc = open(element, 'r')
    result = os.path.splitext(element)[0] + '_AVISO.csv'
    entete = ";".join(entetes) + "\n"
    for ligne in sourc:
        if valeur[0] in ligne:
            contenu += ligne
            sourc = open(result, 'w')
            sourc.write(entete)
            sourc.write(contenu)
            sourc.close()
            dossieraviso()

        else:
            pass


class TraiterfichierAFNET:
    """
    la classe de traitement des fichiers csv AFNET 
    """
    entetes = ENTETES
    valeur = ASN_OPERATEURS
    contenu = ''
    element = 'tester.csv'
    sourc = open(element, 'r')
    result = os.path.splitext(element)[0] + '_AFNET.csv'
    entete = ";".join(entetes) + "\n"
    for ligne in sourc:
        if valeur[1] in ligne:
            contenu += ligne
            sourc = open(result, 'w')
            sourc.write(entete)
            sourc.write(contenu)
            sourc.close()
            dossierafnet()

        else:
            pass


class TraiterfichierMOOVCI:
    """
    la classe de traitement des fichiers csv MOOV-CI 
    """
    entetes = ENTETES
    valeur = ASN_OPERATEURS
    contenu = ''
    element = 'tester.csv'
    sourc = open(element, 'r')
    result = os.path.splitext(element)[0] + '_MOOV-CI.csv'
    entete = ";".join(entetes) + "\n"
    for ligne in sourc:
        if valeur[2] in ligne:
            contenu += ligne
            sourc = open(result, 'w')
            sourc.write(entete)
            sourc.write(contenu)
            sourc.close()
            dossiermoov()

        else:
            pass


class TraiterfichierNSIACI:
    """
    la classe de traitement des fichiers csv NSIA-CI 
    """
    entetes = ENTETES
    valeur = ASN_OPERATEURS
    contenu = ''
    element = 'tester.csv'
    sourc = open(element, 'r')
    result = os.path.splitext(element)[0] + '_NSIA-CI.csv'
    entete = ";".join(entetes) + "\n"
    for ligne in sourc:
        if valeur[3] in ligne:
            contenu += ligne
            sourc = open(result, 'w')
            sourc.write(entete)
            sourc.write(contenu)
            sourc.close()
            dossiernsia()

        else:
            pass


class TraiterfichierVIPNETCT:
    """
    la classe de traitement des fichiers csv VIPNET-CT 
    """
    entetes = ENTETES
    # entetes = str(entetes)
    valeur = ASN_OPERATEURS
    contenu = ''
    element = 'tester.csv'
    sourc = open(element, 'r')
    result = os.path.splitext(element)[0] + '_VIPNET-CT.csv'
    entete = ";".join(entetes) + "\n"
    for ligne in sourc:
        if valeur[4] in ligne:
            contenu += ligne
            sourc = open(result, 'w')
            sourc.write(entete)
            sourc.write(contenu)
            sourc.close()
            dossiervipnet()

        else:
            pass


class TraiterfichierYOOMEE:
    """
    la classe de traitement des fichiers csv YOOMEE 
    """
    entetes = ENTETES
    # entetes = str(entetes)
    valeur = ASN_OPERATEURS
    contenu = ''
    element = 'tester.csv'
    sourc = open(element, 'r')
    result = os.path.splitext(element)[0] + '_YOOMEE.csv'
    entete = ";".join(entetes) + "\n"
    for ligne in sourc:
        if valeur[5] in ligne:
            contenu += ligne
            sourc = open(result, 'w')
            sourc.write(entete)
            sourc.write(contenu)
            sourc.close()
            dossieryoomee()

        else:
            pass
#
#
# if __name__ == '__main__':
#
#     aviso = TraiterfichierAVISO
#     afnet = TraiterfichierAFNET
#     moov = TraiterfichierMOOVCI
#     nsia = TraiterfichierNSIACI
#     vipnet = TraiterfichierVIPNETCT
#     yoomee = TraiterfichierYOOMEE



