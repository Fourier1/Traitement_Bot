#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from traitementbotnet import *
from couleurs import *
from emailbot import *
from config import DATE_TRAITEMENT
from compression import *
from creerdoc import *
from copierfichier import *


print("\t\t\t\t\t\t\033[93m                               ___       ___\033[1;m")
print("\t\t\t\t\t\t\033[93m                              |   \_____/   |\033[1;m")
print("\t\t\t\t\t\t\033[93m                             /  |\/     \/|  \\    \033[1;m")
print("\t\t\t\t\t\t\033[93m                             \_/ | /\ /\ | \_/\033[1;m")
print("\t\t\t\t\t\t\033[97m ____  ____ _____ _____  __   _ \033[1;m \033[93m|_\/ \/_| \033[97m _____   ____   ____\033[1;m")
print("\t\t\t\t\t\t\033[97m|___/  |___ |     |    | | \  | \033[1;m\033[93m/   \o/   \ \033[97m|    \ |    | | ___\033[1;m")
print("\t\t\t\t\t\t\033[97m|   \_ |___ |____ |____| |  \_| \033[1;m\033[93m\___/'\___/ \033[97m|____/ |____| |____| v0.8\033[1;m")

print('\n\n \t\t\t', DATE_TRAITEMENT, '\n')

print(""+T+"[!] " "\033[91m" + " Démarrer en tant que user ! \n" + color.END)
print(color.BOLD + "\n|-----   ARTCI - CI-Cert      -----|")
print(color.WARNING + "\n|-----   1 Outil - 5 choix    -----|")
print(color.DARKCYAN + "\n|----- Bienvenu dans Botnet ! -----|")
print(color.OKBLUE + "\n\n \t\t\t\t\t\t\t 1 : *** RECUPERATION DES FICHIERS SOUS FORME COMPPRESSER SUR LE SERVEUR SHADOWS *** ")
print("  \n \t\t\t\t\t\t\t 2 : *** DECOMPRESSION DES FICHIERS ZIP *** ")
print("  \n \t\t\t\t\t\t\t 3 : *** TRAITEMENT DES FICHIERS RECUPPERE DU SERVEUR SHADOWS *** ")
print("  \n \t\t\t\t\t\t\t 4 : *** COMCOMPRESSION DES FICHIERS en .ZIP *** ")
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
        print("en cour ....")

    if choice == "2":

        print("  \n \t\t\t\t\t\t\t 2 : *** DECOMPRESSION DES FICHIERS ZIP *** ")
        print("en cour ....")

    if choice == "3":

        print("  \n \t\t\t\t\t\t\t TRAITEMENT DES FICHIERS RECUPPERER ")
        # try:

        aviso = TraiterfichierAVISO.aviso(None)
        afnet = TraiterfichierAFNET.afnet(None)
        moov = TraiterfichierMOOVCI.moov(None)
        nsia = TraiterfichierNSIACI.nsia(None)
        vipnet = TraiterfichierVIPNET.vipnet(None)
        yoomee = TraiterfichierYOOMEE.yoomee(None)

        print(" \n \t\t\t\t Fin du traitement !")

        # except NameError as e:
        #     print(" the %s !" % e, '')

    if choice == "4":

        print("  \n \t\t\t\t\t\t\t 2 : *** COMPRESSION DES FICHIERS ZIP *** ")

        zipdirectory('AVISO.zip', 'AVISO')
        zipdirectory('AFNET.zip', 'AFNET')
        zipdirectory('NSIA.zip', 'NSIA')
        zipdirectory('MOOV.zip', 'MOOV')
        zipdirectory('VIPNET.zip', 'VIPNET')
        zipdirectory('YOOMEE.zip', 'YOOMEE')

        dossiercompression()
        Copycompr()

        print(" Fin de compression des dossiers !")

    if choice == "5":

        print("  \n \t\t\t\t\t\t\t ENVOIE DES FICHIERS TRIATER AU DIFFERENTS OPERATEURS ")

        envoiemailaviso()
        envoiemailafnet()
        envoiemailmoov()
        envoiemailvipnet()
        envoiemailnsia()
        envoiemailyoomee()

        print("Fin d\'envoi d'email aus différents opérateurs !")

    if choice == "10":
        print("  \t\t\t\t\t Merci !")
        sys.exit(1)
