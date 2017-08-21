#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
from config import ENTETES, ASN_OPERATEURS
from creerdoc import dossiermoov, dossieraviso, dossierafnet, dossiernsia, dossiervipnet, dossieryoomee
from copierfichier import Copyafnet, Copyaviso, Copymoov, Copynsia, Copynvipnet, Copyyoomee


class TraiterfichierAVISO:
    """
    la classe de traitement des fichiers csv AVISO 
    """
    def aviso(self):

        entetes = ENTETES
        # valeur = ASN_OPERATEURS
        contenu = ''
        element = 'tester.csv'
        sourc = open(element, 'r')
        result = os.path.splitext(element)[0] + '_AVISO.csv'
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

        entetes = ENTETES
        # valeur = ASN_OPERATEURS
        contenu = ''
        element = 'tester.csv'
        sourc = open(element, 'r')
        result = os.path.splitext(element)[0] + '_AFNET.csv'
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

        entetes = ENTETES
        # valeur = ASN_OPERATEURS
        contenu = ''
        element = 'tester.csv'
        sourc = open(element, 'r')
        result = os.path.splitext(element)[0] + '_MOOV-CI.csv'
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

        entetes = ENTETES
        # valeur = ASN_OPERATEURS
        contenu = ''
        element = 'tester.csv'
        sourc = open(element, 'r')
        result = os.path.splitext(element)[0] + '_NSIA-CI.csv'
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

        entetes = ENTETES
        # entetes = str(entetes)
        # valeur = ASN_OPERATEURS
        contenu = ''
        element = 'tester.csv'
        sourc = open(element, 'r')
        result = os.path.splitext(element)[0] + '_VIPNET.csv'
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

        entetes = ENTETES
        # entetes = str(entetes)
        # valeur = ASN_OPERATEURS
        contenu = ''
        element = 'tester.csv'
        sourc = open(element, 'r')
        result = os.path.splitext(element)[0] + '_YOOMEE.csv'
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
