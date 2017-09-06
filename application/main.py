#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import socket

from application.compression import Compress
from application.decom import decomp
from application.config import DATE_TRAITEMENT
from application.copierfichier import *
from application.couleurs import *
from application.creerdoc import *
from application.traitementbotnet import *
from application.config import NOM, SYSTEM, VERSION
from application.config import NOM_SERVICE, NOM_STRUCTURE
from application.emailbot import *
from application.deplacer_docer import deplcer_doc_a_traiter

print("\t\t\t\t\t\t\t\t\t\t\033[93m                               ___       ___\033[1;m")
print("\t\t\t\t\t\t\t\t\t\t\033[93m                              |   \_____/   |\033[1;m")
print("\t\t\t\t\t\t\t\t\t\t\033[93m                             /  |\/     \/|  \\    \033[1;m")
print("\t\t\t\t\t\t\t\t\t\t\033[93m                             \_/ | /\ /\ | \_/\033[1;m")
print("\t\t\t\t\t\t\t\t\t\t\033[97m ____  ____ _____ _____  __   _ \033[1;m \033[93m|_\/ \/_| \033[97m _____   ____   ____\033[1;m")
print("\t\t\t\t\t\t\t\t\t\t\033[97m|___/  |___ |     |    | | \  | \033[1;m\033[93m/   \o/   \ \033[97m|    \ |    | | ___\033[1;m")
print("\t\t\t\t\t\t\t\t\t\t\033[97m|   \_ |___ |____ |____| |  \_| \033[1;m\033[93m\___/'\___/ \033[97m|____/ |____| |____| v0.5 fourier\033[1;m")

print('\n\n \t\t\t', DATE_TRAITEMENT, '\n')

print(""+T+"[!] " "\033[91m" + " Démarrer en tant que user ! \n" + color.END)
print(color.BOLD + "\n|-----   ARTCI - CI-Cert      -----| \t\t\t\t\t\t\t\t\t\t\t\t\t %s " % NOM_STRUCTURE)
print(color.WARNING + "\n|-----   1 Outil - 5 choix    -----| \t\t\t\t\t\t\t\t\t\t\t\t\t\t %s " % NOM_SERVICE)
print(color.DARKCYAN + "\n|----- Bienvenu: %s  -----|" % NOM)
print(color.DARKCYAN + "\n|----- System: %s , Version: %s  -----|" % (SYSTEM, VERSION))
print(color.OKBLUE + "\n\n \t\t\t\t\t\t\t 1 : *** RECUPERATION DES FICHIERS SOUS FORME COMPPRESSER SUR LE SERVEUR SHADOWS (manuellement) *** ")
print("  \n \t\t\t\t\t\t\t 2 : *** DECOMPRESSION DES FICHIERS ZIP *** ")
print("  \n \t\t\t\t\t\t\t 3 : *** TRAITEMENT DES FICHIERS RECUPPERE DU SERVEUR SHADOWS *** ")
print("  \n \t\t\t\t\t\t\t 4 : *** CONCOMPRESSION DES FICHIERS en .ZIP *** ")
print("  \n \t\t\t\t\t\t\t 5 : *** ENVOIE DES FICHIERS TRIATER AU DIFFERENTS OPERATEURS ***")
# print("  \n \t\t\t\t\t\t\t 6 : *** INTERFACE WEB ***")
print(color.RED + "  \n \t\t\t\t\t\t\t 10 : *** QUITTER ***")


# demarer en tand que admin
# if not os.geteuid() == 0:
#     sys.exit("\033[1;31mPlease run dethis script as root!\033[0m")

while True:

    choice = input('\033[1;91mEnter votre choix: \033[1;m ')

    if choice == "1":

        print("\n\n \t\t\t\t\t\t\t RECUPPERATION DES FICHIERS SOUS FORME COMPPRESSER SUR LE SERVEUR SHADOWS ")
        print("en cour ................................................................. .................................................................")

    if choice == "2":

        print("  \n \t\t\t\t\t\t\t 2 : *** DECOMPRESSION DES FICHIERS ZIP *** ")
        print("en cour ................................. .................................................................................................")
        # decompresion des fichier
        decomp()

        print("Fini la décompression")
        # deplacer les dossier a traiter
        deplcer_doc_a_traiter()
        # cretion des doc de rengement de zip
        dossiertraitementZIP()
        try:
            CopycomprZIP()
        except FileNotFoundError as e:
            print('fichier pas trouver %s ' % e)

    if choice == "3":

        print("  \n \t\t\t\t\t\t\t TRAITEMENT DES FICHIERS RECUPPERER ")
        print("en cour ..................................... .............................................................................................")

        aviso = TraiterfichierAVISO.aviso(None)
        afnet = TraiterfichierAFNET.afnet(None)
        moov = TraiterfichierMOOVCI.moov(None)
        nsia = TraiterfichierNSIACI.nsia(None)
        vipnet = TraiterfichierVIPNET.vipnet(None)
        yoomee = TraiterfichierYOOMEE.yoomee(None)

        print(" \n \t\t\t\t Fin du traitement !")
        # deplacer les dossiers zip apres decompression
        CopycomprZIP()

    if choice == "4":

        print("  \n \t\t\t\t\t\t\t 2 : *** COMPRESSION DES FICHIERS ZIP *** ")
        print("en cour .................................. ................................................................................................")
        # compression des ficher
        comp = Compress()
        # copie des fichier dans le dossier de compression
        dossiercompression()
        Copycompr()

    if choice == "5":

        print("  \n \t\t\t\t\t\t\t ENVOIE DES FICHIERS TRIATER AU DIFFERENTS OPERATEURS ")
        print("en cour .............................. ....................................................................................................")

        listdoc = ['AVISO', 'AFNET', 'MOOV', 'NSIA', 'VIPNET', 'YOOMEE']
        try:
            envoiemailaviso()
            envoiemailafnet()
            envoiemailmoov()
            envoiemailvipnet()
            envoiemailnsia()
            envoiemailyoomee()
            print("\n\t\t\t\t\t\t\tFin d\'envoi d'email aus différents opérateurs !")
        except FileNotFoundError as e:
            print(" vérifier les fichiers à envoyés %s " % e)
        except socket.gaierror as e:
            print(" vérifier vootre connexilon  %s " % e.errno)
        except OSError as e:
            print('erreur de démarrage du server %s ' % e)

        try:
            dest = '/home/fourier_saint/PycharmProjects/traite/application/DOC_COMP'
            source = '/home/fourier_saint/PycharmProjects/traite/DOC_COMP'
            shutil.move(dest, source)
        except FileNotFoundError as e:
            print('')

    if choice == "10":
        # ranger les dossiers csv apres utraitement
        dossierCSV()
        try:
            CopycomprCSV()
        except FileNotFoundError as e:
            print('fichier pas trouver %s ' % e)

        print(" \n \t\t\t\t\t\t\t\t\t\t\t\t Merci !")
        sys.exit(1)
