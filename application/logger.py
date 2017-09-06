#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
from logging.handlers import RotatingFileHandler

from application.config import LOGGING_FILE_DIR


def handler(drapau, level, formatter, mode='a', max_bytes=102400000, backup_count=20, encoding="utf-8"):
    """
    handler correspond à la sortie des logs et logger à l'entrée, cote programme
    :param str drapau: les flag
    :param int level: le niveau respective de sensibilité
    :param Formatter formatter: le format désiré du méssage
    :param str mode: le mode d'ecriture
    :param int max_bytes: la taille maximal
    :param int backup_count: le nombre de sovegarde
    :param str encoding: encodage des log
    :return: handlaer
    :rtype RotatingFileHandler
    """
    dra = str(drapau)
    path = LOGGING_FILE_DIR
    _file = "../log/%s/%s.log" % (dra.lower(), dra.lower())
    filename = os.path.join(path, _file)
    hand = logging.handlers.RotatingFileHandler(filename, mode=mode,
                                                maxBytes=max_bytes,
                                                backupCount=backup_count,
                                                encoding=encoding)
    hand.setFormatter(formatter)
    hand.setLevel(level)

    return hand


def get_log():
    """
    creation du log 
    :return: log instance
    """
    # recuperation du format
    formatter = logging.Formatter("%(asctime)s -- %(levelname)s -- %(threaName)s -- %(funcName)s -- %(message)s")
    # creation du log
    logger = logging.getLogger("log")
    logger.setLevel(logging.DEBUG)
    # ajouter les diff"rents niveaux
    logger.addHandler(handler('DEBUG', logging.DEBUG, formatter))
    logger.addHandler(handler('INFO', logging.INFO, formatter))
    logger.addHandler(handler('WARNING', logging.WARNING, formatter))
    logger.addHandler(handler('ERROR', logging.ERROR, formatter))
    logger.addHandler(handler('CRITICAL', logging.CRITICAL, formatter))

    return logger

LOGGER = get_log()