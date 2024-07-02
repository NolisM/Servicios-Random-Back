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

# url, config de Yelp
apiKeyYelp = '_6_rV7LoJIPfdfUCMHwJ8lIEA9MNKbHnIdAa-dm8WhVVaULxzOYqXO-jqPzh9Olea235l9nolhzuv6MefjWRX6LejrUGSN6-DJezCIEGCyPWQ3ks0oVH3xH2dqw1ZnYx'
apiYelpUrl = 'https://api.yelp.com/v3/events/awesome-event'
headersYelp = {
    'accept': 'application/json',
    'authorization': f'Bearer {apiKeyYelp}',
}

#solicitud get Yelp
response_yelp = requests.get(apiYelpUrl, headers=headersYelp)
if response_yelp.status_code == 200:
    data_yelp = response_yelp.json()
    for event in data_yelp.get('events', []):
        fsq_id = event.get('id')
        name = event.get('name')
        ubicacion = event.get('location', {}).get('address1', '')
        icono = ''  
        
        # Inserto ala bd
        cursor.execute('''
            INSERT INTO destinos (customer_id, name, customer_name, ubicacion, icono)
            VALUES (%s, %s, %s, %s, %s)
        ''', (fsq_id, name, name, ubicacion, icono))
        conexion.commit()
else:
    print('Error al obtener los datos de Yelp:', response_yelp.status_code)

# url, config de Foursquare
apiUrl = 'https://api.foursquare.com/v3/places/search'
apiKeyFoursquare = 'fsq3buQ3sQjU/VUhFJxh7dVe8/1AMnf65GT0l4vUU+iWqFg='
headersFoursquare = {
    'accept': 'application/json',
    'Authorization': f'Bearer {apiKeyFoursquare}',
}

params = {
    'll': '-31.4167,-64.1833',
    'radius': 100000,
    'v': '20220101',
}

# solicitud get Fourquare
response_foursquare = requests.get(apiUrl, headers=headersFoursquare, params=params)
if response_foursquare.status_code == 200:
    data_foursquare = response_foursquare.json()
    for place in data_foursquare.get('results', []):
        fsq_id = place.get('fsq_id')
        name = place.get('name')
        ubicacion = place.get('location', {}).get('formatted_address', '')
        icono = place.get('categories', [])[0].get('icon', {}).get('prefix', '') + '64' + place.get('categories', [])[0].get('icon', {}).get('suffix', '')

        # Inserto a la bd
        cursor.execute('''
            INSERT INTO destinos (customer_id, name, customer_name, ubicacion, icono)
            VALUES (%s, %s, %s, %s, %s)
        ''', (fsq_id, name, name, ubicacion, icono))
        conexion.commit()
else:
    print('Error al obtener los datos de Foursquare:', response_foursquare.status_code)

cursor.close()
conexion.close()
