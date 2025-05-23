import unittest
import sys
sys.path.append("src")
from controller.PropiedadesController import PropiedadesController
from model.propiedades import Propiedad

class TestPropiedades(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        PropiedadesController.eliminar_tabla()
        PropiedadesController.crear_tabla()

    def test_insertar_1(self):
        propiedad = Propiedad(None, "Calle 123", 150000.0, "Casa", 10, "2024-01-01 10:00:00")
        PropiedadesController.insertar(propiedad)
        resultado = PropiedadesController.buscar_propiedad(propiedad.id)
        self.assertTrue(self.propiedades_iguales(resultado, propiedad))

    def test_insertar_2(self):
        propiedad = Propiedad(None, "Avenida 456", 250000.0, "Apartamento", 20, "2024-02-01 11:00:00")
        PropiedadesController.insertar(propiedad)
        resultado = PropiedadesController.buscar_propiedad(propiedad.id)
        self.assertTrue(self.propiedades_iguales(resultado, propiedad))

    def test_insertar_3(self):
        propiedad = Propiedad(None, "Carrera 789", 350000.0, "Oficina", 30, "2024-03-01 12:00:00")
        PropiedadesController.insertar(propiedad)
        resultado = PropiedadesController.buscar_propiedad(propiedad.id)
        self.assertTrue(self.propiedades_iguales(resultado, propiedad))

    def test_modificar_1(self):
        propiedad_original = Propiedad(None, "Diagonal 101", 400000.0, "Casa", 40, "2024-04-01 13:00:00")
        PropiedadesController.insertar(propiedad_original)
        id_modificar = propiedad_original.id
        PropiedadesController.eliminar_tabla()
        PropiedadesController.crear_tabla()
        propiedad_modificada = Propiedad(None, "Diagonal 101", 450000.0, "Casa", 40, "2024-04-01 13:00:00")
        PropiedadesController.insertar(propiedad_modificada)
        resultado = PropiedadesController.buscar_propiedad(propiedad_modificada.id)
        self.assertTrue(self.propiedades_iguales(resultado, propiedad_modificada))

    def test_modificar_2(self):
        propiedad_original = Propiedad(None, "Diagonal 202", 500000.0, "Apartamento", 50, "2024-05-01 14:00:00")
        PropiedadesController.insertar(propiedad_original)
        id_modificar = propiedad_original.id
        PropiedadesController.eliminar_tabla()
        PropiedadesController.crear_tabla()
        propiedad_modificada = Propiedad(None, "Diagonal 202", 550000.0, "Apartamento", 50, "2024-05-01 14:00:00")
        PropiedadesController.insertar(propiedad_modificada)
        resultado = PropiedadesController.buscar_propiedad(propiedad_modificada.id)
        self.assertTrue(self.propiedades_iguales(resultado, propiedad_modificada))

    def test_modificar_3(self):
        propiedad_original = Propiedad(None, "Diagonal 303", 600000.0, "Oficina", 60, "2024-06-01 15:00:00")
        PropiedadesController.insertar(propiedad_original)
        id_modificar = propiedad_original.id
        PropiedadesController.eliminar_tabla()
        PropiedadesController.crear_tabla()
        propiedad_modificada = Propiedad(None, "Diagonal 303", 650000.0, "Oficina", 60, "2024-06-01 15:00:00")
        PropiedadesController.insertar(propiedad_modificada)
        resultado = PropiedadesController.buscar_propiedad(propiedad_modificada.id)
        self.assertTrue(self.propiedades_iguales(resultado, propiedad_modificada))

    def test_buscar_1(self):
        propiedad = Propiedad(None, "Transversal 101", 700000.0, "Casa", 70, "2024-07-01 16:00:00")
        PropiedadesController.insertar(propiedad)
        resultado = PropiedadesController.buscar_propiedad(propiedad.id)
        self.assertTrue(self.propiedades_iguales(resultado, propiedad))

    def test_buscar_2(self):
        propiedad = Propiedad(None, "Transversal 202", 800000.0, "Apartamento", 80, "2024-08-01 17:00:00")
        PropiedadesController.insertar(propiedad)
        resultado = PropiedadesController.buscar_propiedad(propiedad.id)
        self.assertTrue(self.propiedades_iguales(resultado, propiedad))

    def test_buscar_3(self):
        propiedad = Propiedad(None, "Transversal 303", 900000.0, "Oficina", 90, "2024-09-01 18:00:00")
        PropiedadesController.insertar(propiedad)
        resultado = PropiedadesController.buscar_propiedad(propiedad.id)
        self.assertTrue(self.propiedades_iguales(resultado, propiedad))

    @staticmethod
    def propiedades_iguales(prop1, prop2):
        if not prop1 or not prop2:
            return False
        return (
            prop1.direccion == prop2.direccion and
            float(prop1.valor) == float(prop2.valor) and
            prop1.tipo == prop2.tipo and
            prop1.propietario_id == prop2.propietario_id and
            str(prop1.fecha_registro) == str(prop2.fecha_registro)
        )

if __name__ == "__main__":
    unittest.main(verbosity=2)