# FROM LIB
from flask import Flask, request, render_template
from routes import *
from Modulos.Manipulation.Manipulation import Analise

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

