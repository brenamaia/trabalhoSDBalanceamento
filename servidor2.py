#!/usr/bin/python
from flask import Flask, jsonify, request
import string
import psutil

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
	return jsonify({'Message': "Servidor 2 executando"})

@app.route('/<name>', methods=['GET', 'POST'])
def main(name):
	
	name = name.split(" ")
	num = len(name)	
	
	data = {
	    "Quantidade de palavras: ": num
	}

	return jsonify(data), 200

@app.route('/status', methods=['GET', 'POST'])
def status():
	cpu = psutil.cpu_percent()
	data = {
	    "CPU": cpu
	}
	print("CPU SERVIDOR 2 = ", data["CPU"])
	return jsonify(data), 200

if __name__ == '__main__':
	app.run(debug=True, host= '192.168.0.125', port=5002)
