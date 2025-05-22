import sys
sys.path.append("")  # Para importar secret_config desde la raíz

import psycopg2
from src.model.propiedades import Propiedad
import secret_config

class PropiedadesController:

    @staticmethod
    def crear_tabla():
        """Crea la tabla de propiedades en la BD"""
        cursor = PropiedadesController.obtener_cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS propiedades (
                id SERIAL PRIMARY KEY,
                direccion VARCHAR(255) NOT NULL,
                valor NUMERIC(15, 2) NOT NULL,
                tipo VARCHAR(50),
                propietario_id INT,
                fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def eliminar_tabla():
        """Elimina la tabla de propiedades de la BD"""
        cursor = PropiedadesController.obtener_cursor()
        cursor.execute("DROP TABLE IF EXISTS propiedades CASCADE;")
        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def borrar_todo():
        """Elimina todos los registros de la tabla propiedades"""
        cursor = PropiedadesController.obtener_cursor()
        cursor.execute("DROP TABLE IF EXISTS propiedades CASCADE;")
        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def insertar(propiedad: Propiedad):
        """Inserta una propiedad en la tabla"""
        cursor = PropiedadesController.obtener_cursor()
        cursor.execute("""
            INSERT INTO propiedades (
                direccion, valor, tipo, propietario_id, fecha_registro
            ) VALUES (%s, %s, %s, %s, %s)
        """, (
            propiedad.direccion,
            propiedad.valor,
            propiedad.tipo,
            propiedad.propietario_id,
            propiedad.fecha_registro
        ))
        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def buscar_propiedad(propiedad_id: int):
        """Busca una propiedad por id"""
        cursor = PropiedadesController.obtener_cursor()
        cursor.execute("""
            SELECT id, direccion, valor, tipo, propietario_id, fecha_registro
            FROM propiedades WHERE id = %s;
        """, (propiedad_id,))
        fila = cursor.fetchone()
        cursor.close()
        if fila:
            return Propiedad(*fila)
        return None

    @staticmethod
    def obtener_cursor():
        """Crea la conexión a la base de datos y retorna un cursor"""
        connection = psycopg2.connect(
            database=secret_config.PGDATABASE,
            user=secret_config.PGUSER,
            password=secret_config.PGPASSWORD,
            host=secret_config.PGHOST,
        )
        return connection.cursor()