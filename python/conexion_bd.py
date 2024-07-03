import requests
import mysql.connector
from mysql.connector import errorcode

# Conexion bd
try:
    conexion = mysql.connector.connect(user='root',
                                       password='',
                                       host='127.0.0.1',
                                       database='tourfy_bd')
    cursor = conexion.cursor()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error con el nombre de usuario o la contraseña")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base de datos no existe")
    else:
        print(err)
    exit(1)


# url, config 
apiUrl = 'https://api.foursquare.com/v3/places/search'
apiKeyFoursquare = 'fsq3buQ3sQjU/VUhFJxh7dVe8/1AMnf65GT0l4vUU+iWqFg='
headersFoursquare = {
    'accept': 'application/json',
    'Authorization': str(f'{apiKeyFoursquare}').replace("'", "`"),
}

params = {
    'll': '-31.4167,-64.1833',
    'radius': 100000,
    'v': '20220101',
}

# solicitud get 
response_foursquare = requests.get(apiUrl, headers=headersFoursquare, params=params)
print("Foursquare status code:", response_foursquare.status_code)
print("Foursquare response:", response_foursquare.json())

cursor.close()
conexion.close()

