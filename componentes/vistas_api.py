# Vistas para la arquitectura API REST
from flask import jsonify
from flask import request

from main import app
from componentes.modelos import Destino
from componentes.modelos import Consulta

@app.route("/api/destinos", methods=['GET'])
def api_destinos():
    destinos = Destino.obtener()
    datos = [destino.__dict__ for destino in destinos]
    return jsonify(datos)

@app.route("/api/consultas", methods=['GET'])
def api_consultas():
    consultas = Consulta.obtener()
    datos = [consulta.__dict__ for consulta in consultas]
    return jsonify(datos)