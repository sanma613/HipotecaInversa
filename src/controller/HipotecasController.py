import sys
sys.path.append("")  # Para importar secret_config desde la raíz

import psycopg2
from src.model.Hipotecas import Hipoteca
from secret_config import SecretConfig

class HipotecasController:

    @staticmethod
    def sincronizar_secuencia():
        cursor = HipotecasController.obtener_cursor()
        cursor.execute("SELECT setval('hipotecas_id_seq', (SELECT MAX(id) FROM hipotecas));")
        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def crear_tabla():
        """Crea la tabla de hipotecas en la BD"""
        cursor = HipotecasController.obtener_cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS hipotecas (
                id SERIAL PRIMARY KEY,
                cliente_id INT REFERENCES clientes(id),
                propiedad_id INT REFERENCES propiedades(id),
                total_cuotas INT NOT NULL,
                tasa_interes_mensual NUMERIC(5, 2) NOT NULL,
                ingreso_mensual NUMERIC(15, 2),
                deuda_total NUMERIC(15, 2),
                fecha_inicio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                estado VARCHAR(20) NOT NULL DEFAULT 'activa'
            );
        """)
        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def eliminar_tabla():
        """Elimina la tabla de hipotecas de la BD"""
        cursor = HipotecasController.obtener_cursor()
        cursor.execute("DROP TABLE IF EXISTS hipotecas CASCADE;")
        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def borrar_todo():
        """Elimina todos los registros de la tabla hipotecas"""
        cursor = HipotecasController.obtener_cursor()
        cursor.execute("DELETE FROM hipotecas;")
        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def insertar(hipoteca: Hipoteca):
        """Inserta una hipoteca en la tabla"""
        cursor = HipotecasController.obtener_cursor()
        cursor.execute("""
            INSERT INTO hipotecas (
                cliente_id, propiedad_id, total_cuotas, tasa_interes_mensual,
                ingreso_mensual, deuda_total, fecha_inicio, estado
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            hipoteca.cliente_id,
            hipoteca.propiedad_id,
            hipoteca.total_cuotas,
            hipoteca.tasa_interes_mensual,
            hipoteca.ingreso_mensual,
            hipoteca.deuda_total,
            hipoteca.fecha_inicio,
            hipoteca.estado
        ))
        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def buscar_hipoteca(hipoteca_id: int):
        """Busca una hipoteca por id"""
        cursor = HipotecasController.obtener_cursor()
        cursor.execute("""
            SELECT id, cliente_id, propiedad_id, total_cuotas, tasa_interes_mensual,
            ingreso_mensual, deuda_total, fecha_inicio, estado
            FROM hipotecas WHERE id = %s;
        """, (hipoteca_id,))
        fila = cursor.fetchone()
        cursor.close()
        if fila:
            return Hipoteca(*fila)
        return None

    @staticmethod
    def listar_todos():
        """Devuelve una lista de todas las hipotecas"""
        cursor = HipotecasController.obtener_cursor()
        cursor.execute("""
            SELECT id, cliente_id, propiedad_id, total_cuotas, tasa_interes_mensual,
                   ingreso_mensual, deuda_total, fecha_inicio, estado
            FROM hipotecas;
        """)
        filas = cursor.fetchall()
        cursor.close()
        return [Hipoteca(*fila) for fila in filas]

    @staticmethod
    def obtener_cursor():
        config = SecretConfig()
        db_config = config.get_postgres_config()
        conn = psycopg2.connect(**db_config)
        return conn.cursor()