import unittest
import sys
sys.path.append("src")
from controller.HipotecasController import HipotecasController
from model.Hipotecas import Hipoteca

class TestHipotecas(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        HipotecasController.eliminar_tabla()
        HipotecasController.crear_tabla()

    def setUp(self):
        HipotecasController.eliminar_tabla()
        HipotecasController.crear_tabla()

    def crear_hipoteca_dummy(self, id_hipoteca, deuda_total, estado):
        # Crear cliente si no existe
        from controller.ClientesController import ClientesController
        from model.Clientes import Cliente
        try:
            ClientesController.insertar(Cliente(1, "Cliente Test", 50, "Calle Test", "123456789", "test@mail.com", "2024-01-01 00:00:00"))
        except Exception:
            pass 
        hipoteca = Hipoteca(
            id_hipoteca, 1, 1, 12, 0.05, 1000.0, deuda_total, "2024-01-01 00:00:00", estado
        )
        HipotecasController.insertar(hipoteca)
        HipotecasController.sincronizar_secuencia()
        return hipoteca

    def test_insertar_1(self):
        hipoteca = self.crear_hipoteca_dummy(301, 50000.0, "activa")
        resultado = HipotecasController.buscar_hipoteca(301)
        self.assertTrue(self.hipotecas_iguales(resultado, hipoteca))

    def test_insertar_2(self):
        hipoteca = self.crear_hipoteca_dummy(302, 60000.0, "activa")
        resultado = HipotecasController.buscar_hipoteca(302)
        self.assertTrue(self.hipotecas_iguales(resultado, hipoteca))

    def test_insertar_3(self):
        hipoteca = self.crear_hipoteca_dummy(303, 70000.0, "activa")
        resultado = HipotecasController.buscar_hipoteca(303)
        self.assertTrue(self.hipotecas_iguales(resultado, hipoteca))

    def test_modificar_1(self):
        hipoteca = self.crear_hipoteca_dummy(304, 80000.0, "activa")
        HipotecasController.eliminar_tabla()
        HipotecasController.crear_tabla()
        hipoteca_mod = Hipoteca(304, 1, 1, 12, 0.05, 1000.0, 81000.0, "2024-01-01 00:00:00", "activa")
        HipotecasController.insertar(hipoteca_mod)
        resultado = HipotecasController.buscar_hipoteca(304)
        self.assertTrue(self.hipotecas_iguales(resultado, hipoteca_mod))

    def test_modificar_2(self):
        hipoteca = self.crear_hipoteca_dummy(305, 90000.0, "activa")
        HipotecasController.eliminar_tabla()
        HipotecasController.crear_tabla()
        hipoteca_mod = Hipoteca(305, 1, 1, 12, 0.05, 1000.0, 91000.0, "2024-01-01 00:00:00", "activa")
        HipotecasController.insertar(hipoteca_mod)
        resultado = HipotecasController.buscar_hipoteca(305)
        self.assertTrue(self.hipotecas_iguales(resultado, hipoteca_mod))

    def test_modificar_3(self):
        hipoteca = self.crear_hipoteca_dummy(306, 100000.0, "activa")
        HipotecasController.eliminar_tabla()
        HipotecasController.crear_tabla()
        hipoteca_mod = Hipoteca(306, 1, 1, 12, 0.05, 1000.0, 101000.0, "2024-01-01 00:00:00", "activa")
        HipotecasController.insertar(hipoteca_mod)
        resultado = HipotecasController.buscar_hipoteca(306)
        self.assertTrue(self.hipotecas_iguales(resultado, hipoteca_mod))

    def test_buscar_1(self):
        hipoteca = self.crear_hipoteca_dummy(307, 110000.0, "activa")
        resultado = HipotecasController.buscar_hipoteca(307)
        self.assertTrue(self.hipotecas_iguales(resultado, hipoteca))

    def test_buscar_2(self):
        hipoteca = self.crear_hipoteca_dummy(308, 120000.0, "activa")
        resultado = HipotecasController.buscar_hipoteca(308)
        self.assertTrue(self.hipotecas_iguales(resultado, hipoteca))

    def test_buscar_3(self):
        hipoteca = self.crear_hipoteca_dummy(309, 130000.0, "activa")
        resultado = HipotecasController.buscar_hipoteca(309)
        self.assertTrue(self.hipotecas_iguales(resultado, hipoteca))

    @staticmethod
    def hipotecas_iguales(h1, h2):
        if not h1 or not h2:
            return False
        return (
            h1.id == h2.id and
            h1.cliente_id == h2.cliente_id and
            h1.propiedad_id == h2.propiedad_id and
            h1.total_cuotas == h2.total_cuotas and
            float(h1.tasa_interes_mensual) == float(h2.tasa_interes_mensual) and
            float(h1.ingreso_mensual) == float(h2.ingreso_mensual) and
            float(h1.deuda_total) == float(h2.deuda_total) and
            str(h1.fecha_inicio) == str(h2.fecha_inicio) and
            str(h1.estado) == str(h2.estado)
        )

if __name__ == "__main__":
    unittest.main(verbosity=2)