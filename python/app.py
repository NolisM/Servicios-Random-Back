from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# conexión a la bd
bd = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='tourfy_bd'
)
cursor = bd.cursor()

# Ruta para obtener destinos
@app.route('/api/destinos', methods=['GET'])
def get_destinos():
    query = "SELECT id, nombre, ubicacion, url_img FROM destinos"
    cursor.execute(query)
    destinos = []
    for (id, nombre, ubicacion, url_img) in cursor:
        destino = {
            'id': id,
            'nombre': nombre,
            'ubicacion': ubicacion,
            'url_img': url_img
        }
        destinos.append(destino)
    return jsonify(destinos)

if __name__ == '__main__':
    app.run(debug=True)
