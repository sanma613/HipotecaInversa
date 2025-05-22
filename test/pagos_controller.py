import unittest
import sys
sys.path.append("src")
from controller.PagosController import PagosController
from model.Pagos import Pago

class TestPagos(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        PagosController.eliminar_tabla()
        PagosController.crear_tabla()

    # ----------- TEST INSERTAR -----------
    def test_insertar_1(self):
        pago = Pago(1, 101, 1500.0, "2024-01-01 10:00:00")
        PagosController.insertar(pago)
        resultado = PagosController.buscar_pago(pago.id)
        self.assertTrue(self.pagos_iguales(resultado, pago))

    def test_insertar_2(self):
        pago = Pago(2, 102, 2500.0, "2024-02-01 11:00:00")
        PagosController.insertar(pago)
        resultado = PagosController.buscar_pago(pago.id)
        self.assertTrue(self.pagos_iguales(resultado, pago))

    def test_insertar_3(self):
        pago = Pago(3, 103, 3500.0, "2024-03-01 12:00:00")
        PagosController.insertar(pago)
        resultado = PagosController.buscar_pago(pago.id)
        self.assertTrue(self.pagos_iguales(resultado, pago))

    # ----------- TEST MODIFICAR -----------
    def test_modificar_1(self):
        pago_original = Pago(4, 104, 4000.0, "2024-04-01 13:00:00")
        PagosController.insertar(pago_original)
        PagosController.eliminar_tabla()
        PagosController.crear_tabla()
        pago_modificado = Pago(4, 104, 4500.0, "2024-04-01 13:00:00")
        PagosController.insertar(pago_modificado)
        resultado = PagosController.buscar_pago(4)
        self.assertTrue(self.pagos_iguales(resultado, pago_modificado))

    def test_modificar_2(self):
        pago_original = Pago(5, 105, 5000.0, "2024-05-01 14:00:00")
        PagosController.insertar(pago_original)
        PagosController.eliminar_tabla()
        PagosController.crear_tabla()
        pago_modificado = Pago(5, 105, 5500.0, "2024-05-01 14:00:00")
        PagosController.insertar(pago_modificado)
        resultado = PagosController.buscar_pago(5)
        self.assertTrue(self.pagos_iguales(resultado, pago_modificado))

    def test_modificar_3(self):
        pago_original = Pago(6, 106, 6000.0, "2024-06-01 15:00:00")
        PagosController.insertar(pago_original)
        PagosController.eliminar_tabla()
        PagosController.crear_tabla()
        pago_modificado = Pago(6, 106, 6500.0, "2024-06-01 15:00:00")
        PagosController.insertar(pago_modificado)
        resultado = PagosController.buscar_pago(6)
        self.assertTrue(self.pagos_iguales(resultado, pago_modificado))

    # ----------- TEST BUSCAR -----------
    def test_buscar_1(self):
        pago = Pago(7, 107, 7000.0, "2024-07-01 16:00:00")
        PagosController.insertar(pago)
        resultado = PagosController.buscar_pago(7)
        self.assertTrue(self.pagos_iguales(resultado, pago))

    def test_buscar_2(self):
        pago = Pago(8, 108, 8000.0, "2024-08-01 17:00:00")
        PagosController.insertar(pago)
        resultado = PagosController.buscar_pago(8)
        self.assertTrue(self.pagos_iguales(resultado, pago))

    def test_buscar_3(self):
        pago = Pago(9, 109, 9000.0, "2024-09-01 18:00:00")
        PagosController.insertar(pago)
        resultado = PagosController.buscar_pago(9)
        self.assertTrue(self.pagos_iguales(resultado, pago))

    @staticmethod
    def pagos_iguales(pago1, pago2):
        if not pago1 or not pago2:
            return False
        return (
            pago1.id == pago2.id and
            pago1.hipoteca_id == pago2.hipoteca_id and
            float(pago1.monto) == float(pago2.monto) and
            str(pago1.fecha_pago) == str(pago2.fecha_pago)
        )

if __name__ == "__main__":
    unittest.main()