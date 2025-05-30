import sys
sys.path.append("")  # Para importar secret_config desde la raíz

import psycopg2
from src.model.propiedades import Propiedad
from secret_config import SecretConfig

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
        cursor = PropiedadesController.obtener_cursor()
        cursor.execute("""
            INSERT INTO propiedades (
                direccion, valor, tipo, propietario_id, fecha_registro
            ) VALUES (%s, %s, %s, %s, %s)
            RETURNING id
        """, (
            propiedad.direccion,
            propiedad.valor,
            propiedad.tipo,
            propiedad.propietario_id,
            propiedad.fecha_registro
        ))
        propiedad.id = cursor.fetchone()[0]  
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
    def listar_todos():
        """Devuelve una lista de todas las propiedades"""
        cursor = PropiedadesController.obtener_cursor()
        cursor.execute("""
            SELECT id, direccion, valor, tipo, propietario_id, fecha_registro
            FROM propiedades;
        """)
        filas = cursor.fetchall()
        cursor.close()
        return [Propiedad(*fila) for fila in filas]

    @staticmethod
    def obtener_cursor():
        config = SecretConfig()
        db_config = config.get_postgres_config()
        conn = psycopg2.connect(**db_config)
        return conn.cursor()
    
    @staticmethod
    def eliminarbyid(cliente_id: int):
        cursor= PropiedadesController.obtener_cursor()
        cursor.execute("DELETE FROM propiedades WHERE id = %s", (cliente_id,))
        cursor.connection.commit()
        cursor.close ()
