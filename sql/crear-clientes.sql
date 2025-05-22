CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad INT NOT NULL,
    direccion VARCHAR(255),
    telefono VARCHAR(15),
    email VARCHAR(100),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);