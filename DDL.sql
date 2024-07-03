CREATE DATABASE IF NOT EXISTS tourfy_bd;

USE tourfy_bd;


CREATE TABLE destinos (
    id INT NOT NULL AUTO_INCREMENT ,
    nombre VARCHAR(100) NOT NULL,
    ubicacion VARCHAR(255) NOT NULL,
    url_img VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE consulta (
   id int(11) NOT NULL AUTO_INCREMENT,
   nombre varchar(50) DEFAULT NULL,
   apellido varchar(50) DEFAULT NULL,
   email varchar(50) DEFAULT NULL,
   telefono varchar(50) DEFAULT NULL,
   mensaje varchar(1000) DEFAULT NULL,
   tipo varchar(50) DEFAULT NULL,
   estado tinyint(1) NOT NULL,
   PRIMARY KEY (id)
);
