import unittest
import sys
sys.path.append("src")
from controller.ClientesController import ClientesController
from model.Clientes import Cliente

class TestClientes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ClientesController.eliminar_tabla()
        ClientesController.crear_tabla()

    def setUp(self):
        ClientesController.eliminar_tabla()
        ClientesController.crear_tabla()

    def crear_cliente_dummy(self, id_cliente, nombre, edad, direccion, telefono, email, fecha_registro):
        cliente = Cliente(
            id_cliente, nombre, edad, direccion, telefono, email, fecha_registro
        )
        ClientesController.insertar(cliente)
        return cliente

    def test_insertar_1(self):
        cliente = self.crear_cliente_dummy(
            1, "Juan Pérez", 30, "Calle 1", "123456789", "juan@mail.com", "2024-01-01 00:00:00"
        )
        resultado = ClientesController.buscar_cliente(1)
        self.assertTrue(self.clientes_iguales(resultado, cliente))

    def test_insertar_2(self):
        cliente = self.crear_cliente_dummy(
            2, "Ana López", 40, "Calle 2", "987654321", "ana@mail.com", "2024-01-02 00:00:00"
        )
        resultado = ClientesController.buscar_cliente(2)
        self.assertTrue(self.clientes_iguales(resultado, cliente))

    def test_insertar_3(self):
        cliente = self.crear_cliente_dummy(
            3, "Carlos Ruiz", 50, "Calle 3", "555555555", "carlos@mail.com", "2024-01-03 00:00:00"
        )
        resultado = ClientesController.buscar_cliente(3)
        self.assertTrue(self.clientes_iguales(resultado, cliente))

    def test_modificar_1(self):
        cliente = self.crear_cliente_dummy(
            4, "Laura Gómez", 60, "Calle 4", "444444444", "laura@mail.com", "2024-01-04 00:00:00"
        )
        ClientesController.eliminar_tabla()
        ClientesController.crear_tabla()
        cliente_mod = Cliente(4, "Laura Gómez", 61, "Calle 4", "444444444", "laura@mail.com", "2024-01-04 00:00:00")
        ClientesController.insertar(cliente_mod)
        resultado = ClientesController.buscar_cliente(4)
        self.assertTrue(self.clientes_iguales(resultado, cliente_mod))

    def test_modificar_2(self):
        cliente = self.crear_cliente_dummy(
            5, "Pedro Torres", 70, "Calle 5", "333333333", "pedro@mail.com", "2024-01-05 00:00:00"
        )
        ClientesController.eliminar_tabla()
        ClientesController.crear_tabla()
        cliente_mod = Cliente(5, "Pedro Torres", 71, "Calle 5", "333333333", "pedro@mail.com", "2024-01-05 00:00:00")
        ClientesController.insertar(cliente_mod)
        resultado = ClientesController.buscar_cliente(5)
        self.assertTrue(self.clientes_iguales(resultado, cliente_mod))

    def test_modificar_3(self):
        cliente = self.crear_cliente_dummy(
            6, "Sofía Díaz", 80, "Calle 6", "222222222", "sofia@mail.com", "2024-01-06 00:00:00"
        )
        ClientesController.eliminar_tabla()
        ClientesController.crear_tabla()
        cliente_mod = Cliente(6, "Sofía Díaz", 81, "Calle 6", "222222222", "sofia@mail.com", "2024-01-06 00:00:00")
        ClientesController.insertar(cliente_mod)
        resultado = ClientesController.buscar_cliente(6)
        self.assertTrue(self.clientes_iguales(resultado, cliente_mod))

    def test_buscar_1(self):
        cliente = self.crear_cliente_dummy(
            7, "Mario Castro", 90, "Calle 7", "111111111", "mario@mail.com", "2024-01-07 00:00:00"
        )
        resultado = ClientesController.buscar_cliente(7)
        self.assertTrue(self.clientes_iguales(resultado, cliente))

    def test_buscar_2(self):
        cliente = self.crear_cliente_dummy(
            8, "Lucía Vega", 100, "Calle 8", "000000000", "lucia@mail.com", "2024-01-08 00:00:00"
        )
        resultado = ClientesController.buscar_cliente(8)
        self.assertTrue(self.clientes_iguales(resultado, cliente))

    def test_buscar_3(self):
        cliente = self.crear_cliente_dummy(
            9, "Andrés Gil", 110, "Calle 9", "999999999", "andres@mail.com", "2024-01-09 00:00:00"
        )
        resultado = ClientesController.buscar_cliente(9)
        self.assertTrue(self.clientes_iguales(resultado, cliente))

    @staticmethod
    def clientes_iguales(c1, c2):
        if not c1 or not c2:
            return False
        return (
            c1.nombre == c2.nombre and
            c1.edad == c2.edad and
            c1.direccion == c2.direccion and
            c1.telefono == c2.telefono and
            c1.email == c2.email and
            str(c1.fecha_registro) == str(c2.fecha_registro)
        )

if __name__ == "__main__":
    unittest.main(verbosity=2)