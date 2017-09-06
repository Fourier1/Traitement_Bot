#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path


globals()
chemindoc = os.getcwd()


def dossieraviso():
    if not os.path.exists('AVISO'):
        os.mkdir(chemindoc + '/AVISO')


def dossierafnet():

    if not os.path.exists('AFNET'):
        os.mkdir(chemindoc + '/AFNET')


def dossiermoov():

    if not os.path.exists('MOOV'):

        os.mkdir(chemindoc + '/MOOV')


def dossiernsia():

    if not os.path.exists('NSIA'):
        os.mkdir(chemindoc + '/NSIA')


def dossiervipnet():

    if not os.path.exists('VIPNET'):
        os.mkdir(chemindoc + '/VIPNET')


def dossieryoomee():

    if not os.path.exists('YOOMEE'):
        os.mkdir(chemindoc + '/YOOMEE')


def dossiercompression():

    if not os.path.exists('DOC_COMP'):
        os.mkdir(chemindoc + '/DOC_COMP')


def dossiertraitementZIP():

    if not os.path.exists('DOC_TREMENT_ZIP'):
        os.mkdir(chemindoc + '/DOC_TREMENT_ZIP')


def dossierCSV():

    if not os.path.exists('DOC_CSV'):
        os.mkdir(chemindoc + '/DOC_CSV')


