import mysql.connector

# Establecer la conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="tourfy"
)

datos_destinos = [
    ('Coffee Shop cafe especialidad', 'obispo trejo 774, 5000', 'https://ss3.4sqi.net/img/categories_v2/food/coffeeshop_'),
    ('Chilli Street Food', 'X5000BOE, Fructuoso Rivera 273, X5000BOE Córdoba', 'https://ss3.4sqi.net/img/categories_v2/nightlife/pub_'),
    ('Patio De La Cañada', 'Av. Figueroa Alcorta, 360, X5000 KFQ, Córdoba', 'https://ss3.4sqi.net/img/categories_v2/food/argentinian_'),
    ('Manzana Jesuitica', 'Obispo Trejo 300-398, X5000 IYH, Córdoba', 'https://ss3.4sqi.net/img/categories_v2/building/government_monument_'),
    ('Iglesia De Los Capuchinos', 'Buenos Aires 600, centro, Córdoba, Argentina', 'https://ss3.4sqi.net/img/categories_v2/building/government_monument_'),
    ('Francis Bar & Charcutería', 'Galería Barrio, Dr. T. Achaval Rodriguez 244 Locales 13 y 14, X5000 Córdoba', 'https://ss3.4sqi.net/img/categories_v2/nightlife/pub_'),
    ('La Capke – ᴄᴏꜰᴇᴇ & ʙʀᴜɴᴄʜ', 'Fructuoso Rivera 260, X5000 Córdoba', 'https://ss3.4sqi.net/img/categories_v2/food/coffeeshop_'),
    ('Jardin Botanico', 'Francisco Yunyent 5491, Córdoba', 'https://ss3.4sqi.net/img/categories_v2/building/government_monument_'),
    ('Mil Grullas 𝑦 𝑢𝑛𝑎 𝑡𝑎𝑧𝑎 𝑑𝑒 𝑡𝑒́', 'Belgrano 893, X5000JQQ JQQ, Córdoba', 'https://ss3.4sqi.net/img/categories_v2/food/tearoom_'),
    ('Pizza Madre', 'Av. Marcelo T. de Alvear 277, X5000 Córdoba', 'https://ss3.4sqi.net/img/categories_v2/food/pizza_'),
    ('Grabeat', 'Santiago Derqui 88, X5000, Córdoba', 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0d/6c/6f/d5/grabeat.jpg')
]

cursor = conexion.cursor()

# Iterar sobre los datos y ejecutar la consulta de inserción
for nombre, ubicacion, imagen in datos_destinos:
    sql_insert = "INSERT INTO destino (nombre, ubicacion, imagen) VALUES (%s, %s, %s)"
    datos = (nombre, ubicacion, imagen)
    cursor.execute(sql_insert, datos)

conexion.commit()

# Mostrar los datos insertados 
cursor.execute("SELECT * FROM destino")
resultados = cursor.fetchall()
for resultado in resultados:
    print(resultado)

cursor.close()
conexion.close()
