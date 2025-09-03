from flask import Flask, request, jsonify
from flask_cors import CORS  # Importar CORS
import os
import pandas as pd

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas y orígenes

print("Version 37")


df = pd.read_csv("miniBase.csv")


@app.route('/')
def home():
    return jsonify({"message": "Bienvenido a la API de Datos de Crimen"})

@app.route('/query/')
def answer_query():
    query = request.args.get('query', '')
    try:
        return jsonify({"response": {"Hola":10}})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)