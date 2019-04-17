#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

arq = open('/home/nupasd-ufpi/trabalho5SD/ArquivoGerado.txt', 'r')
texto = arq.read()
arq.close()

texto = requests.post("http://192.168.0.115:5000/%s"%(texto))
print(texto.json())





