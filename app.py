# FROM LIB
from flask import Flask, request, render_template
from Modulos.Manipulation.Manipulation import Analise
# IMPORT LIB
import json

ans = Analise()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    data = request.get_json()
    modelo = data.get("modelo")
    comprimento = data.get("comprimento")
    envergadura = data.get("envergadura")
    altura = data.get("altura")
    raio_curva = data.get("raio_curva")
    distancia_tremPouso_pavimenato = data.get("distancia_tremPouso_pavimenato")
    distancia_tremPouso_taxi = data.get("distancia_tremPouso_taxi")
    codigo = data.get("codigo")
    largura_pista = data.get("largura_pista")
    largura_faixa = data.get("largura_faixa")
    acostamento = data.get("acostamento")
    desvio_lateral = data.get("desvio_lateral")
    mtow = data.get("mtow")
    largura_pista_taxi = data.get("largura_pista_taxi")
    margem_seguranca = data.get("margem_seguranca")
    
    ans.Calc_analise(, distancia_tremPouso_pavimenato, distancia_tremPouso_taxi, acostamento, largura_pista, largura_faixa, desvio_lateral, margem_seguranca)
    ans.Constructor_infoJSON(codigo, largura_pista, largura_pista_taxi)
    ans.ConstructorJSON()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
