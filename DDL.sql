CREATE DATABASE IF NOT EXISTS tourfy_bd;

USE tourfy_bd;


CREATE TABLE destinos (
    id INT NOT NULL AUTO_INCREMENT ,
    customer_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    customer_name VARCHAR(100) NOT NULL,
    ubicacion VARCHAR(255) NOT NULL,
    icono VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE consultas (
    id INT NOT NULL AUTO_INCREMENT,
    order_id INT NOT NULL ,
    name VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    telefono VARCHAR(50),
    mensaje VARCHAR(1000) NOT NULL,
    type VARCHAR(50) NOT NULL,
    state BOOLEAN NOT NULL,
    PRIMARY KEY (id)
);

