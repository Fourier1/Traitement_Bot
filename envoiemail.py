# Importation des modules

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

try:

    Fromadd = "saintfourieronesyme@gmail.com"
    Toadd = "warrensaint1@gmail.com"

    cc = ["fouriersaint@gmail.com", "formation.cour01@gmail.com"]
    # Spécification des destinataires en copie carbone (cas de plusieurs destinataires)
    bcc = "juniorwognin34@gmail.com"
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

    message['Subject'] = "testmail"
    # Spécification de l'objet de votre mail
    msg = "VOTRE MESSAGE Fourier onesyme"
    # Message à envoyer
    message.attach(MIMEText(msg.encode('utf-8'), 'plain', 'utf-8'))
    # Attache du message à l'objet "message", et encodage en UTF-8

    # piece_jointe = ['tester.zip', 'teston.zip']
    nom_fichier = 'tester.zip'
    # Spécification du nom de la pièce jointe
    piece = open(nom_fichier, "rb")
    # Ouverture du fichier
    part = MIMEBase('application', 'octet-stream')
    # Encodage de la pièce jointe en Base64
    part.set_payload((piece).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "piece=%s ; filename= %s" % (nom_fichier))
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
    serveur.sendmail(Fromadd, Toadd, texte)
    # Envoi du mail
    serveur.quit()
    # Déconnexion du serveur

    print("\n \t\t\tEMAIL ENVOYE AVEC SUCCES")

except smtplib.SMTPAuthenticationError as e:

        print(" Erreur d'envoie de mail Authentification requis ! %s \n" % e)