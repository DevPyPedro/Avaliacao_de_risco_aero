from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    data = request.get_json()
    with open('Dados.json', 'w') as f:
        json.dump(data, f)
    return 'Dados salvos com sucesso!', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
