CREATE TABLE hipotecas (
    id SERIAL PRIMARY KEY,
    cliente_id INT REFERENCES clientes(id),
    propiedad_id INT REFERENCES propiedades(id),
    total_cuotas INT NOT NULL,
    tasa_interes_mensual NUMERIC(5, 2) NOT NULL,
    ingreso_mensual NUMERIC(15, 2),
    deuda_total NUMERIC(15, 2),
    fecha_inicio TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);