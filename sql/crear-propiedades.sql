CREATE TABLE propiedades (
    id SERIAL PRIMARY KEY,
    cliente_id INT REFERENCES clientes(id),
    direccion VARCHAR(255) NOT NULL,
    valor_estimado NUMERIC(15, 2) NOT NULL,
    porcentaje_precio_real NUMERIC(5, 2) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);