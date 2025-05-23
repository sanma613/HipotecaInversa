import sys
sys.path.append("")  # Para importar secret_config desde la raíz

import psycopg2
from src.model.Pagos import Pago
from secret_config import SecretConfig

class PagosController:

    @staticmethod
    def crear_tabla():
        """Crea la tabla de pagos en la BD"""
        cursor = PagosController.obtener_cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pagos (
                id SERIAL PRIMARY KEY,
                hipoteca_id INT REFERENCES hipotecas(id),
                monto NUMERIC(15, 2) NOT NULL,
                fecha_pago TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def eliminar_tabla():
        """Elimina la tabla de pagos de la BD"""
        cursor = PagosController.obtener_cursor()
        cursor.execute("DROP TABLE IF EXISTS pagos;")
        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def borrar_todo():
        """Elimina todos los registros de la tabla pagos"""
        cursor = PagosController.obtener_cursor()
        cursor.execute("DELETE FROM pagos;")
        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def insertar(pago: Pago):
        cursor = PagosController.obtener_cursor()
        cursor.execute(
            """
            INSERT INTO pagos (hipoteca_id, monto, fecha_pago)
            VALUES (%s, %s, %s)
            """,
            (pago.hipoteca_id, pago.monto, pago.fecha_pago)
        )
        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def buscar_pago(pago_id: int):
        """Busca un pago por id"""
        cursor = PagosController.obtener_cursor()
        cursor.execute("""
            SELECT id, hipoteca_id, monto, fecha_pago
            FROM pagos WHERE id = %s;
        """, (pago_id,))
        fila = cursor.fetchone()
        cursor.close()
        if fila:
            return Pago(*fila)
        return None

    @staticmethod
    def listar_todos():
        """Devuelve una lista de todos los pagos"""
        cursor = PagosController.obtener_cursor()
        cursor.execute("""
            SELECT id, hipoteca_id, monto, fecha_pago
            FROM pagos;
        """)
        filas = cursor.fetchall()
        cursor.close()
        return [Pago(*fila) for fila in filas]

    @staticmethod
    def obtener_cursor():
        config = SecretConfig()
        db_config = config.get_postgres_config()
        conn = psycopg2.connect(**db_config)
        return conn.cursor()