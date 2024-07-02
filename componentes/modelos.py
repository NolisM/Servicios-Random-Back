# Clases que corresponden a entidades en la BBDD
from base_db.config_db import conexion
from base_db.dml import Tabla
from auxiliares.cifrado import encriptar

class Destino(Tabla):
    tabla = 'destino'
    conexion = conexion
    campos = ('id', 'nombre', 'ubicacion')
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)
        
class Consulta(Tabla):
    tabla = 'consulta'
    conexion = conexion
    campos = ('id', 'nombre', 'apellido', 'email', 'telefono', 'mensaje', 'tipo', 'estado')
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)
    