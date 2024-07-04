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
    print(datos)
    return jsonify(datos)
  
@app.route("/api/destinos", methods=['POST'])
def crear_consulta():
    
    if request.method == 'POST':
        datos = request.json
        print('datos=>', datos)
        destino_nueva = Destino(
            datos['nombre'],
            datos['ubicacion'],
            datos['imagen'],
        )
        print('destino=>', destino_nueva)
        destino_nueva = destino_nueva.guardar_db()
        respuesta = {'mensaje': destino_nueva}
        
    else:
        respuesta = {'mensaje': 'no se recibieron datos.'}

    return jsonify(respuesta)

@app.route("/api/consultas", methods=['GET'])
def api_consultas():
    consultas = Consulta.obtener()
    datos = [consulta.__dict__ for consulta in consultas]
    return jsonify(datos)

@app.route("/api/consultas", methods=['POST'])
def crear_consulta():
    
    if request.method == 'POST':
        datos = request.json
        print('datos=>', datos)
        consulta_nueva = Consulta(
            datos['nombre'],
            datos['apellido'],
            datos['email'],
            datos['telefono'],
            datos['mensaje'],
            datos['tipo'],
            datos['estado'],
        )
        print('consulta=>', consulta_nueva)
        consulta_nueva = consulta_nueva.guardar_db()
        respuesta = {'mensaje': consulta_nueva}
        
    else:
        respuesta = {'mensaje': 'no se recibieron datos.'}

    return jsonify(respuesta)
  
@app.route("/api/consultas", methods=['DELETE'])
def eliminar_consulta():
    
    if request.method == 'DELETE':
        datos = request.json 
        print('datos=>', datos)
        consulta_modif = Consulta.modificar(datos)
        respuesta = {'mensaje': consulta_modif}
        
        if consulta_modif:
            respuesta = {'mensaje': 'se elimino con exito'}
        else:
            respuesta = {'mensaje': 'Algo salió mal!'}
    
    else:
        respuesta = {'mensaje': 'no se recibieron datos.'}
        
    return jsonify(respuesta)
