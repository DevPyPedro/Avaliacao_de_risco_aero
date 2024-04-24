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
    bitola = float(data.get("bitola"))
    peso_vazia = float(data.get("peso_vazia"))
    envergadura = float(data.get("envergadura"))
    distancia_tremPouso_pavimenato = float(data.get("distancia_tremPouso_pavimenato"))
    distancia_tremPouso_taxi = float(data.get("distancia_tremPouso_taxi"))
    codigo = data.get("codigo")
    largura_pista = float(data.get("largura_pista"))
    largura_faixa = float(data.get("largura_faixa"))
    acostamento = float(data.get("acostamento"))
    desvio_lateral = float(data.get("desvio_lateral"))
    mtow = float(data.get("mtow"))
    largura_pista_taxi = float(data.get("largura_pista_taxi"))
    margem_seguranca = float(data.get("margem_seguranca"))
    ans.Calc_analise(peso_vazia,bitola,distancia_tremPouso_pavimenato, distancia_tremPouso_taxi, acostamento, largura_pista, largura_faixa,envergadura, desvio_lateral, margem_seguranca)
    ans.Constructor_infoJSON(codigo, largura_pista, largura_pista_taxi, mtow)
    ans.ConstructorJSON(codigo)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
