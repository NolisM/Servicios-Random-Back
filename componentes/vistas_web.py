# Vistas según patrón MVT (Model View Template)
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

from main import app
from componentes.modelos import Destino
from componentes.modelos import Consulta

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/destinos')
@app.route('/destinos/<mensaje>')
def destinos(mensaje=None):
    destinos = Destino.obtener()
    return render_template('./modelos/destinos.html', destinos=destinos, mensaje=mensaje)

@app.route('/consultas')
@app.route('/consultas/<mensaje>')
def consultas(mensaje=None):
    consultas = Consulta.obtener()
    return render_template('./modelos/consultas.html', consultas=consultas, mensaje=mensaje)


tablas = {
    "destino": Destino,
    "consulta": Consulta
}

@app.route('/<id>/<tipo>/detalle')
def ver_detalle(id, tipo):
    return render_template("./modelos/crud/detalle.html", 
                           datos=tablas[tipo].obtener('id', id), 
                           tipo=tipo)

@app.route('/<id>/<tipo>/eliminar')
def eliminar(id, tipo):
    respuesta = tablas[tipo].eliminar(id)
    return redirect(url_for(tipo + "s", mensaje=respuesta))

@app.route('/<id>/<tipo>/modificar', methods=['POST'])
def modificar(id, tipo):
    
    if request.method == 'POST':
        datos = dict(request.form)
        datos['id'] = id
        respuesta = tablas[tipo].modificar(datos)
        
    return redirect(url_for(tipo + "s", mensaje=respuesta))

@app.route('/<tipo>/crear', methods=['GET', 'POST'])
def crear(tipo):
    
    if request.method == 'POST':
        datos = dict(request.form).values()
        nvo_registro = tablas[tipo](*list(datos))
        respuesta = nvo_registro.guardar_db()
        return redirect(url_for(tipo + "s", mensaje=respuesta))        
    
    modelo = tablas[tipo].campos[1:]  
    return render_template('./modelos/crud/crear.html', tipo=tipo, modelo=modelo)


@app.route('/api/')
def api_docu():
    return render_template('./api/docu.html')

@app.errorhandler(404)
def lanzar_error(error):
    return render_template("./404.html", ctx=error)