import unittest
import sys
sys.path.append("src")
from controller.PagosController import PagosController
from model.Pagos import Pago

# Importa los modelos/controladores de Hipotecas para crear hipotecas dummy
from controller.HipotecasController import HipotecasController
from model.Hipotecas import Hipoteca

class TestPagos(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        PagosController.eliminar_tabla()
        PagosController.crear_tabla()
        HipotecasController.eliminar_tabla()
        HipotecasController.crear_tabla()

    def crear_hipoteca_dummy(self, id_hipoteca):
        from controller.ClientesController import ClientesController
        from model.Clientes import Cliente
        from controller.PropiedadesController import PropiedadesController
        from model.propiedades import Propiedad

        cliente = Cliente(1, "Nombre", 30, "direccion", "telefono", "email")
        ClientesController.insertar(cliente)
        propiedad = Propiedad(1, "Direccion", 100000.0, "Casa", 1, "2024-01-01 00:00:00")
        PropiedadesController.insertar(propiedad)

        # Ajusta el número y orden de argumentos según tu clase Hipoteca
        hipoteca = Hipoteca(
            id_hipoteca,    # id
            1,              # cliente_id
            1,              # propiedad_id
            12,             # total_cuotas
            0.05,           # tasa_interes_mensual
            1000.0,         # ingreso_mensual
            50000.0,        # deuda_total
            "2024-01-01 00:00:00",  # fecha_inicio
            "activa"        # estado
        )
        HipotecasController.insertar(hipoteca)

    def test_insertar_1(self):
        self.crear_hipoteca_dummy(101)
        pago = Pago(None, 101, 1500.0, "2024-01-01 10:00:00")
        PagosController.insertar(pago)
        resultado = PagosController.buscar_pago(pago.id)
        self.assertTrue(self.pagos_iguales(resultado, pago))

    def test_insertar_2(self):
        self.crear_hipoteca_dummy(102)
        pago = Pago(None, 102, 2500.0, "2024-02-01 11:00:00")
        PagosController.insertar(pago)
        resultado = PagosController.buscar_pago(pago.id)
        self.assertTrue(self.pagos_iguales(resultado, pago))

    def test_insertar_3(self):
        self.crear_hipoteca_dummy(103)
        pago = Pago(None, 103, 3500.0, "2024-03-01 12:00:00")
        PagosController.insertar(pago)
        resultado = PagosController.buscar_pago(pago.id)
        self.assertTrue(self.pagos_iguales(resultado, pago))

    def test_modificar_1(self):
        PagosController.eliminar_tabla()
        PagosController.crear_tabla()
        HipotecasController.eliminar_tabla()
        HipotecasController.crear_tabla()
        self.crear_hipoteca_dummy(104)
        pago_original = Pago(None, 104, 4000.0, "2024-04-01 13:00:00")
        PagosController.insertar(pago_original)
        PagosController.eliminar_tabla()
        PagosController.crear_tabla()
        HipotecasController.eliminar_tabla()
        HipotecasController.crear_tabla()
        self.crear_hipoteca_dummy(104)
        pago_modificado = Pago(None, 104, 4500.0, "2024-04-01 13:00:00")
        PagosController.insertar(pago_modificado)
        resultado = PagosController.buscar_pago(pago_modificado.id)
        self.assertTrue(self.pagos_iguales(resultado, pago_modificado))

    def test_modificar_2(self):
        PagosController.eliminar_tabla()
        PagosController.crear_tabla()
        HipotecasController.eliminar_tabla()
        HipotecasController.crear_tabla()
        self.crear_hipoteca_dummy(105)
        pago_original = Pago(None, 105, 5000.0, "2024-05-01 14:00:00")
        PagosController.insertar(pago_original)
        PagosController.eliminar_tabla()
        PagosController.crear_tabla()
        HipotecasController.eliminar_tabla()
        HipotecasController.crear_tabla()
        self.crear_hipoteca_dummy(105)
        pago_modificado = Pago(None, 105, 5500.0, "2024-05-01 14:00:00")
        PagosController.insertar(pago_modificado)
        resultado = PagosController.buscar_pago(pago_modificado.id)
        self.assertTrue(self.pagos_iguales(resultado, pago_modificado))

    def test_modificar_3(self):
        PagosController.eliminar_tabla()
        PagosController.crear_tabla()
        HipotecasController.eliminar_tabla()
        HipotecasController.crear_tabla()
        self.crear_hipoteca_dummy(106)
        pago_original = Pago(None, 106, 6000.0, "2024-06-01 15:00:00")
        PagosController.insertar(pago_original)
        PagosController.eliminar_tabla()
        PagosController.crear_tabla()
        HipotecasController.eliminar_tabla()
        HipotecasController.crear_tabla()
        self.crear_hipoteca_dummy(106)
        pago_modificado = Pago(None, 106, 6500.0, "2024-06-01 15:00:00")
        PagosController.insertar(pago_modificado)
        resultado = PagosController.buscar_pago(pago_modificado.id)
        self.assertTrue(self.pagos_iguales(resultado, pago_modificado))

    def test_buscar_1(self):
        self.crear_hipoteca_dummy(107)
        pago = Pago(None, 107, 7000.0, "2024-07-01 16:00:00")
        PagosController.insertar(pago)
        resultado = PagosController.buscar_pago(pago.id)
        self.assertTrue(self.pagos_iguales(resultado, pago))

    def test_buscar_2(self):
        self.crear_hipoteca_dummy(108)
        pago = Pago(None, 108, 8000.0, "2024-08-01 17:00:00")
        PagosController.insertar(pago)
        resultado = PagosController.buscar_pago(pago.id)
        self.assertTrue(self.pagos_iguales(resultado, pago))

    def test_buscar_3(self):
        self.crear_hipoteca_dummy(109)
        pago = Pago(None, 109, 9000.0, "2024-09-01 18:00:00")
        PagosController.insertar(pago)
        resultado = PagosController.buscar_pago(pago.id)
        self.assertTrue(self.pagos_iguales(resultado, pago))

    @staticmethod
    def pagos_iguales(pago1, pago2):
        if not pago1 or not pago2:
            return False
        return (
            pago1.hipoteca_id == pago2.hipoteca_id and
            float(pago1.monto) == float(pago2.monto) and
            str(pago1.fecha_pago) == str(pago2.fecha_pago)
        )

if __name__ == "__main__":
    unittest.main(verbosity=2)