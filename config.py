#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from couleurs import *


DATE_TRAITEMENT = time.strftime('LA DATE DU TRAITEMENT EST : %A %d %B %Y, \n\n\t\t\t ET  L\'HEUR DU TRAITEMENT : %H:%M.', time.localtime())

ASN_OPERATEURS = ['29571', '36974', '37190', '327746', '37381', '37475']

ENTETES = [

    u'timestamp',
    u'ip',
    u'port',
    u'asn',
    u'geo',
    u'region',
    u'city',
    u'hostname',
    u'type',
    u'infection',
    u'url',
    u'agent',
    u'ic_ip',
    u'ic_port',
    u'ic_asn',
    u'ic_geo',
    u'ic_dns',
    u'count',
    u'proxy',
    u'application',
    u'p0f_genre',
    u'p0f_detail',
    u'machine_name',
    u'id',
    u'naics',
    u'sic',
    u'cc_naics',
    u'cc_sic',
    u'sector',
    u'cc_sector',
    u'ssl_cipher',
    u'family',
    u'tag',
    u'public_source',

]

ENTETE = ";".join(ENTETES) + "\n"
