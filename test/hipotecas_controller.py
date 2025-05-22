import unittest
import sys
sys.path.append("src")
from controller.HipotecasController import HipotecasController
from model.Hipotecas import Hipoteca
from controller.ClientesController import ClientesController
from model.Clientes import Cliente
from controller.PropiedadesController import PropiedadesController
from model.propiedades import Propiedad

class TestHipotecas(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        HipotecasController.eliminar_tabla()
        PropiedadesController.eliminar_tabla()
        ClientesController.eliminar_tabla()
        ClientesController.crear_tabla()
        PropiedadesController.crear_tabla()
        HipotecasController.crear_tabla()

    def crear_cliente_dummy(self, id_cliente, edad=30):
        try:
            ClientesController.eliminar(id_cliente)
        except Exception:
            pass
        cliente = Cliente(id_cliente, "Nombre", edad, "direccion", "telefono", "email")
        ClientesController.insertar(cliente)

    def crear_propiedad_dummy(self, id_propiedad, propietario_id=None):
        if propietario_id is None:
            propietario_id = id_propiedad
        try:
            PropiedadesController.eliminar(id_propiedad)
        except Exception:
            pass
        propiedad = Propiedad(id_propiedad, "Direccion", 100000.0, "Casa", propietario_id, "2024-01-01 00:00:00")
        PropiedadesController.insertar(propiedad)

    def test_insertar_1(self):
        self.crear_cliente_dummy(1)
        self.crear_propiedad_dummy(1, 1)
        hipoteca = Hipoteca(1, 1, 1, 12, 0.05, 1000.0, 50000.0, "2024-01-01 10:00:00", "activa")
        HipotecasController.insertar(hipoteca)
        resultado = HipotecasController.buscar_hipoteca(hipoteca.id)
        self.assertTrue(self.hipotecas_iguales(resultado, hipoteca))

    def test_insertar_2(self):
        self.crear_cliente_dummy(2)
        self.crear_propiedad_dummy(2, 2)
        hipoteca = Hipoteca(2, 2, 2, 24, 0.04, 2000.0, 100000.0, "2024-02-01 11:00:00", "activa")
        HipotecasController.insertar(hipoteca)
        resultado = HipotecasController.buscar_hipoteca(hipoteca.id)
        self.assertTrue(self.hipotecas_iguales(resultado, hipoteca))

    def test_insertar_3(self):
        self.crear_cliente_dummy(3)
        self.crear_propiedad_dummy(3, 3)
        hipoteca = Hipoteca(3, 3, 3, 36, 0.03, 3000.0, 150000.0, "2024-03-01 12:00:00", "activa")
        HipotecasController.insertar(hipoteca)
        resultado = HipotecasController.buscar_hipoteca(hipoteca.id)
        self.assertTrue(self.hipotecas_iguales(resultado, hipoteca))

    def test_modificar_1(self):
        self.crear_cliente_dummy(4)
        self.crear_propiedad_dummy(4, 4)
        hipoteca_original = Hipoteca(4, 4, 4, 48, 0.06, 4000.0, 200000.0, "2024-04-01 13:00:00", "activa")
        HipotecasController.insertar(hipoteca_original)
        hipoteca_modificada = Hipoteca(4, 4, 4, 48, 0.07, 4500.0, 210000.0, "2024-04-01 13:00:00", "activa")
        HipotecasController.modificar(hipoteca_modificada)
        resultado = HipotecasController.buscar_hipoteca(hipoteca_modificada.id)
        self.assertTrue(self.hipotecas_iguales(resultado, hipoteca_modificada))

    def test_modificar_2(self):
        self.crear_cliente_dummy(5)
        self.crear_propiedad_dummy(5, 5)
        hipoteca_original = Hipoteca(5, 5, 5, 60, 0.05, 5000.0, 250000.0, "2024-05-01 14:00:00", "activa")
        HipotecasController.insertar(hipoteca_original)
        hipoteca_modificada = Hipoteca(5, 5, 5, 60, 0.06, 5500.0, 260000.0, "2024-05-01 14:00:00", "activa")
        HipotecasController.modificar(hipoteca_modificada)
        resultado = HipotecasController.buscar_hipoteca(hipoteca_modificada.id)
        self.assertTrue(self.hipotecas_iguales(resultado, hipoteca_modificada))

    def test_modificar_3(self):
        self.crear_cliente_dummy(6)
        self.crear_propiedad_dummy(6, 6)
        hipoteca_original = Hipoteca(6, 6, 6, 72, 0.04, 6000.0, 300000.0, "2024-06-01 15:00:00", "activa")
        HipotecasController.insertar(hipoteca_original)
        hipoteca_modificada = Hipoteca(6, 6, 6, 72, 0.045, 6500.0, 310000.0, "2024-06-01 15:00:00", "activa")
        HipotecasController.modificar(hipoteca_modificada)
        resultado = HipotecasController.buscar_hipoteca(hipoteca_modificada.id)
        self.assertTrue(self.hipotecas_iguales(resultado, hipoteca_modificada))

    def test_buscar_1(self):
        self.crear_cliente_dummy(7)
        self.crear_propiedad_dummy(7, 7)
        hipoteca = Hipoteca(7, 7, 7, 84, 0.035, 7000.0, 350000.0, "2024-07-01 16:00:00", "activa")
        HipotecasController.insertar(hipoteca)
        resultado = HipotecasController.buscar_hipoteca(hipoteca.id)
        self.assertTrue(self.hipotecas_iguales(resultado, hipoteca))

    def test_buscar_2(self):
        self.crear_cliente_dummy(8)
        self.crear_propiedad_dummy(8, 8)
        hipoteca = Hipoteca(8, 8, 8, 96, 0.032, 8000.0, 400000.0, "2024-08-01 17:00:00", "activa")
        HipotecasController.insertar(hipoteca)
        resultado = HipotecasController.buscar_hipoteca(hipoteca.id)
        self.assertTrue(self.hipotecas_iguales(resultado, hipoteca))

    def test_buscar_3(self):
        self.crear_cliente_dummy(9)
        self.crear_propiedad_dummy(9, 9)
        hipoteca = Hipoteca(9, 9, 9, 108, 0.03, 9000.0, 450000.0, "2024-09-01 18:00:00", "activa")
        HipotecasController.insertar(hipoteca)
        resultado = HipotecasController.buscar_hipoteca(hipoteca.id)
        self.assertTrue(self.hipotecas_iguales(resultado, hipoteca))

    @staticmethod
    def hipotecas_iguales(hip1, hip2):
        if not hip1 or not hip2:
            return False
        return (
            hip1.cliente_id == hip2.cliente_id and
            hip1.propiedad_id == hip2.propiedad_id and
            hip1.total_cuotas == hip2.total_cuotas and
            float(hip1.tasa_interes_mensual) == float(hip2.tasa_interes_mensual) and
            float(hip1.ingreso_mensual) == float(hip2.ingreso_mensual) and
            float(hip1.deuda_total) == float(hip2.deuda_total) and
            str(hip1.fecha_inicio) == str(hip2.fecha_inicio) and
            hip1.estado == hip2.estado
        )

if __name__ == "__main__":
    unittest.main(verbosity=2)