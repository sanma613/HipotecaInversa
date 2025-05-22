import sys
sys.path.append("")  # Para importar secret_config desde la raíz

import psycopg2
from src.model.Clientes import Cliente
from secret_config import SecretConfig

class ClientesController:

    @staticmethod
    def crear_tabla():
        """Crea la tabla de clientes en la BD"""
        cursor = ClientesController.obtener_cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                edad INT NOT NULL,
                direccion VARCHAR(255),
                telefono VARCHAR(15),
                email VARCHAR(100),
                fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def eliminar_tabla():
        """Elimina la tabla de clientes de la BD"""
        cursor = ClientesController.obtener_cursor()
        cursor.execute("DROP TABLE IF EXISTS clientes CASCADE;")
        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def borrar_todo():
        """Elimina todos los registros de la tabla clientes"""
        cursor = ClientesController.obtener_cursor()
        cursor.execute("DELETE FROM clientes;")
        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def insertar(cliente: Cliente):
        """Inserta un cliente en la tabla"""
        cursor = ClientesController.obtener_cursor()
        cursor.execute("""
            INSERT INTO clientes (
                id, nombre, edad, direccion, telefono, email, fecha_registro
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            cliente.id,
            cliente.nombre,
            cliente.edad,
            cliente.direccion,
            cliente.telefono,
            cliente.email,
            cliente.fecha_registro
        ))
        cursor.connection.commit()
        cursor.close()

    @staticmethod
    def buscar_cliente(cliente_id: int):
        """Busca un cliente por id"""
        cursor = ClientesController.obtener_cursor()
        cursor.execute("""
            SELECT id, nombre, edad, direccion, telefono, email, fecha_registro
            FROM clientes WHERE id = %s;
        """, (cliente_id,))
        fila = cursor.fetchone()
        cursor.close()
        if fila:
            return Cliente(*fila)
        return None

    @staticmethod
    def obtener_cursor():
        config = SecretConfig()
        db_config = config.get_postgres_config()
        conn = psycopg2.connect(**db_config)
        return conn.cursor()