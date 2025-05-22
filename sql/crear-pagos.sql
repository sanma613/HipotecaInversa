CREATE TABLE pagos (
    id SERIAL PRIMARY KEY,
    hipoteca_id INT REFERENCES hipotecas(id),
    monto NUMERIC(15, 2) NOT NULL,
    fecha_pago TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);