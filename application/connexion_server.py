#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import socket

host = '127.0.0.1'
typeport = 80


def Co_server():
    """
    cette fonction nous permetra de nous connecter a un server 
    grace a son url (protocol TCP) et un por dedier
    :return: 
    """
    # tester la creation du socket
    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.errno as e:
        print('Erreur de creation dou socket %s ' % e)
        sys.exit(1)
    # tester si le port est un entier
    try:
        port = int(typeport)
    except ValueError:
        # tester si l'adresse trouve le port
        try:
            port = socket.getservbyname(host, 'tcp')
        except socket.errno as e:
            print('ne trouve pas le port %s ' % e)
            sys.exit(1)
    # tester la connexion
    try:
        soc.connect((host, port))
    except socket.gaierror as e:
        print('erreur d\'adresse de connexion au serveur %s ' % e)
        sys.exit(1)
    except socket.errno as e:
        print('erreur de connexion su serveur %s ' % e)
        sys.exit(1)
    for doc in host:
        if os.path.isdir(doc):
            while 1:
                data = soc.recv(128)
                print(data)
                if data == " ":
                    break
            soc.close()

# if __name__ == '__main__':
#     # Co_server()