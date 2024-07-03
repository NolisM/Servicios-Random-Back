USE tourfy_bd;

-- Insertar datos destinos
INSERT INTO destinos (nombre, ubicacion, url_img)
VALUES
    ('El Papagayo', 'Arturo M Bas 69 (e/ 27 de Abril y Deán Funes), Ciudad de Córdoba, Córdoba, AR, 5000', 'https://ejemplo.com/imagen1.jpg'),
    ('Starbucks', 'Paseo del Buen Pastor, Ciudad de Córdoba, Córdoba, AR, 5000', 'https://ejemplo.com/imagen2.jpg'),
    ('La Vieja Esquina', 'cnr Belgrano & Caseros (esq. Manuel Belgrano), Ciudad de Córdoba, Córdoba, AR, 5000', 'https://ejemplo.com/imagen3.jpg'),
    ('Mil Grullas y una taza de té', 'Belgrano 893 (Achaval Rodriguez), Ciudad de Córdoba, Córdoba, AR, 5000', 'https://ejemplo.com/imagen4.jpg'),
    ('Muy Güemes', 'Fructuoso Rivera 260 (e/ Belgrano y Av. Vélez Sarsfield), Ciudad de Córdoba, Córdoba, AR, 5009', 'https://ejemplo.com/imagen5.jpg'),
    ('Encontrar Té en Hebras', 'Montevideo, 611 (Arturo M Bas), Ciudad de Córdoba, Córdoba, AR, 5000', 'https://ejemplo.com/imagen6.jpg'),
    ('San Pietro', 'Gral. Juan Jose Viamonte 45 (Rosario De Santa Fe), Ciudad de Córdoba, Córdoba, AR, 5000', 'https://ejemplo.com/imagen7.jpg'),
    ('Valdes', 'Justo José de Urquiza 1894 (Esquina Antonio de Viso), Ciudad de Córdoba, Córdoba, AR, 5000', 'https://ejemplo.com/imagen8.jpg'),
    ('Chia Good Food', '4238 Luis de Tejeda, Ciudad de Córdoba, Córdoba, AR, 5009', 'https://ejemplo.com/imagen9.jpg'),
    ('Starbucks', 'Dinosaurio Mall, Ciudad de Córdoba, Córdoba, AR, 5000', 'https://ejemplo.com/imagen10.jpg');

-- Consulta para verificar 
SELECT * FROM destinos;