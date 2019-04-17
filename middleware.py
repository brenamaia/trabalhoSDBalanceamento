#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
import string
import threading
import time
import requests
import psutil
import os
import subprocess


app = Flask(__name__)

ipServidor1= '192.168.0.146'
ipServidor2= '192.168.0.125'
ipMiddleware= '192.168.0.115'

@app.route('/', methods=['GET'])
def home():
	return jsonify({'Message': "Middleware Executando"})


@app.route('/<name>', methods=['GET', 'POST'])
def main(name):
	
	
	

	#recebendo ping dos servidores
	ping = {
		"response1": subprocess.Popen(["ping","-c","5", ipServidor1],stdout = subprocess.PIPE).communicate()[0],
		"response2": subprocess.Popen(["ping","-c","5", ipServidor2],stdout = subprocess.PIPE).communicate()[0]
	}

	print("ping =", ping['response1'], ping['response2'])



	#analisando se os servidores estão disponiveis
	if ('100% packet loss' not in ping['response1']) and ('100% packet loss' not in ping['response2']):
		#nesse caso, ambos estão disponiveis e será verificado o status de uso de CPU
		print("op1 escolhido")

		data1 = {
			"Serv1": requests.post("http://" + ipServidor1 + ":5001/status").json(),
			"Serv2": requests.post("http://" + ipServidor2 + ":5002/status").json()
		}

		print(data1['Serv1']['CPU'], data1['Serv2']['CPU'])

		if (data1['Serv1']['CPU']) < (data1['Serv2']['CPU']):
			print("servidor 1 escolhido")
			data = {
				"": requests.post("http://" + ipServidor1 + ":5001/%s"%(name)).json()
				#"a": "SERVIDOR 1 ESCOLHIDO",
				#"CPU 1": data1['Serv1']['CPU'], 
				#"CPU 2": data1['Serv2']['CPU']
			}
		else:
			print("servidor 2 escolhido")		
			data = {
				"": requests.post("http://" + ipServidor2 +":5002/%s"%(name)).json()
				#"a": "SERVIDOR 2 ESCOLHIDO",
				#"CPU 1": data1['Serv1']['CPU'], 
				#"CPU 2": data1['Serv2']['CPU']
			}		
	


	elif ('100% packet loss' not in ping['response1']) and ('100% packet loss' in ping['response2']):
		#nesse caso, apenas o servidor 1 está disponível
		data = {
			"": requests.post("http://" + ipServidor1 + ":5001/%s"%(name)).json()
			
		}
	elif ('100% packet loss' in ping['response1']) and ('100% packet loss' not in ping['response2']):
		#nesse caso, apenas o servidor 2 está disponível
		data = {
			"": requests.post("http://" + ipServidor2 + ":5002/%s"%(name)).json()
			
		}	
	

	return jsonify(data), 200

if __name__ == '__main__':
	app.run(debug=True, host=ipMiddleware, port=5000, threaded = True)
	



