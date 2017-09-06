# -*- coding:utf-8 -*-
# Importation des modules
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


globals()
Fromadd = "saintfourieronesyme@gmail.com"


def envoiemailaviso():

    try:

        Toadd = "warrensaint1@gmail.com"

        cc = []
        # Spécification des destinataires en copie carbone (cas de plusieurs destinataires)
        bcc = ""
        # Spécification du destinataire en copie cachée (en copie cachée)

        #  Spécification des destinataires
        message = MIMEMultipart()
        # Création de l'objet "message"
        message['From'] = Fromadd
        # Spécification de l'expéditeur
        message['To'] = Toadd
        # Attache du destinataire à l'objet "message"

        message['CC'] = ",".join(cc)
        # Attache des destinataires en copie carbone à l'objet "message" (cas de plusieurs destinataires)
        message['BCC'] = bcc
        # Attache du destinataire en copie cachée à l'objet "message"

        message['Subject'] = "Aviso 00"
        # Spécification de l'objet de votre mail
        msg = " les bots Aviso "
        # Message à envoyer
        message.attach(MIMEText(msg.encode('utf-8'), 'plain', 'utf-8'))
        # Attache du message à l'objet "message", et encodage en UTF-8

        # piece_jointe = ['tester.zip', 'teston.zip']
        listdoc = ['AVISO.zip', 'AFNET.zip', 'MOOV.zip', 'NSIAzip', 'VIPNET.zip', 'YOOMEE.zip']
        ch = os.getcwd() + '/DOC_COMP/'
        print(ch)
        for doc in listdoc:
            if doc in os.listdir(ch):
                # if doc in listdoc:
                if doc == 'AVISO.zip':
                    print(doc)
                    nom_fichier = doc
                    # Spécification du nom de la pièce jointe
                    piece = open(nom_fichier, "rb")
                    # Ouverture du fichier
                    part = MIMEBase('application', 'octet-stream')
                    # Encodage de la pièce jointe en Base64
                    part.set_payload((piece).read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "piece; filename= %s" % nom_fichier)
                    message.attach(part)
                    # Attache de la pièce jointe à l'objet "message"

                    serveur = smtplib.SMTP('smtp.gmail.com', 587)
                    # Connexion au serveur sortant (en précisant son nom et son port)
                    serveur.starttls()
                    # Spécification de la sécurisation
                    serveur.login(Fromadd, "saint02111366")
                    # Authentification
                    texte = message.as_string().encode('utf-8')
                    # piece_jointes = message.as_string().encode('utf-8')
                    # Conversion de l'objet "message" en chaine de caractère et encodage en UTF-8
                    Toadds = [Toadd] + cc + [bcc]
                    # Rassemblement des destinataires
                    serveur.sendmail(Fromadd, Toadds, texte)
                    # Envoi du mail
                    serveur.quit()
                    # Déconnexion du serveur

                    print("\n \t\t\t MAIL AVISO ENVOYER !")

    except smtplib.SMTPAuthenticationError as e:

            print(" Erreur d'envoie de mail Authentification requis ! %s \n" % e)

if __name__ == '__main__':
    envoiemailaviso()
