/*
Fille: app de consola con python.
Autor: Roberto Rico Sandoval.
Versión: V.0.1
Fecha de creación: 12/09/2021
*/

CREATE DATABASE IF NOT EXISTS app_python_consola;
--Especificar el nombre de la base de datos, en donde, se va a trabajar.
USE app_python_consola;

CREATE TABLE usuarios(
    id          int(255) auto_increment not null,
    nombre      varchar(100),
    apellidos   varchar(255),
    email       varchar(255) not null,

    password    varchar(64) not null,
    fecha       date not null,

    -- Restincciones en la base de datos.
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uk_email UNIQUE(email)
    
)ENGINE = InnoDb;


CREATE TABLE notas(
    num         int(255) auto_increment not null,
    usuario_id  int(25) not null,
    titulo      varchar(255) not null,
    descripcion text,
    fecha       date not null,

    -- Restincciones en la base de datos.
    CONSTRAINT pk_notas PRIMARY KEY(num),
    CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE = InnoDb;

