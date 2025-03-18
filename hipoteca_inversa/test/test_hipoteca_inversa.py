import unittest

import sys
sys.path.append("src/model")

from model import hipoteca_inversa

class PruebasHipotecaInversa(unittest.TestCase):

    # 3 Casos de Prueba Normales    
    def test_calcular_hipoteca_inversa_1(self):
        edad = 70
        expectativa_de_vida = 75
        años_de_renta = 5
        total_cuotas = 60
        precio_de_la_vivienda = 200_000_000
        porcentaje_precio_real = 30
        valor_de_la_hipoteca = 60_000_000
        tasa_de_interes_mensual = 10

        resultado_ingreso_mensual_esperado = 1_000_000
        resultado_deuda_total_esperada = 3_338_298_035

        hipoteca = hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

        ingreso_mensual = hipoteca.calcular_ingreso_mensual()
        deuda_total = hipoteca.calcular_deuda_total(ingreso_mensual)

        print("\nCaso Normal 1")
        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    def test_calcular_hipoteca_inversa_2(self):
        edad = 75
        expectativa_de_vida = 88
        años_de_renta = 17
        total_cuotas = 156
        precio_de_la_vivienda = 412_949_945
        porcentaje_precio_real = 50
        valor_de_la_hipoteca = 206_474_973
        tasa_de_interes_mensual = 5.50

        resultado_ingreso_mensual_esperado = 1_323_558
        resultado_deuda_total_esperada = 107_625_171_318

        hipoteca = hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

        ingreso_mensual = hipoteca.calcular_ingreso_mensual()
        deuda_total = hipoteca.calcular_deuda_total(ingreso_mensual)

        print("\nCaso Normal 2")
        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    def test_calcular_hipoteca_inversa_3(self):
        edad = 85
        expectativa_de_vida = 89
        años_de_renta = 4
        total_cuotas = 48
        precio_de_la_vivienda = 619_424_917
        porcentaje_precio_real = 40
        valor_de_la_hipoteca = 247_769_967
        tasa_de_interes_mensual = 4.80

        resultado_ingreso_mensual_esperado = 5_161_874
        resultado_deuda_total_esperada = 957_016_422

        hipoteca = hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

        ingreso_mensual = hipoteca.calcular_ingreso_mensual()
        deuda_total = hipoteca.calcular_deuda_total(ingreso_mensual)

        print("\nCaso Normal 3")
        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    # 3 Casos de Prueba Extraordinarios
    def test_calcular_hipoteca_inversa_total_cuotas_1(self):
        edad = 70
        expectativa_de_vida = 85
        años_de_renta = 20                                       
        total_cuotas = 1
        precio_de_la_vivienda = 908_489_879
        porcentaje_precio_real = 55
        valor_de_la_hipoteca = 499_699_433
        tasa_de_interes_mensual = 1.20

        resultado_ingreso_mensual_esperado = 499_669_433
        resultado_deuda_total_esperada = 505_665_467

        hipoteca = hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

        ingreso_mensual = hipoteca.calcular_ingreso_mensual()
        deuda_total = hipoteca.calcular_deuda_total(ingreso_mensual)

        print("\nCaso Extraordinario 1")
        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    def test_calculos_hipoteca_inversa_tasa_de_interes_0(self):
        edad = 78
        expectativa_de_vida = 90
        años_de_renta = 12
        total_cuotas = 144
        precio_de_la_vivienda = 1_238_849_835
        porcentaje_precio_real = 50
        valor_de_la_hipoteca = 619_424_918
        tasa_de_interes_mensual = 0

        resultado_ingreso_mensual_esperado = 4_301_562
        resultado_deuda_total_esperada = 619_424_918

        hipoteca = hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

        ingreso_mensual = hipoteca.calcular_ingreso_mensual()
        deuda_total = hipoteca.calcular_deuda_total(ingreso_mensual)

        print("\nCaso Extraordinario 2")
        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    def test_calcular_hipoteca_inversa_hipoteca_porcentaje_precio_real_100(self):
        edad = 76
        expectativa_de_vida = 88
        años_de_renta = 12
        total_cuotas = 144
        precio_de_la_vivienda = 743_309_901
        porcentaje_precio_real = 100
        valor_de_la_hipoteca = 743_309_901
        tasa_de_interes_mensual = 1.1

        resultado_ingreso_mensual_esperado = 5_161_874
        resultado_deuda_total_esperada = 1_818_198_009

        hipoteca = hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

        ingreso_mensual = hipoteca.calcular_ingreso_mensual()
        deuda_total = hipoteca.calcular_deuda_total(ingreso_mensual)

        print("\nCaso Extraordinario 3")
        print("Advertencia: La hipoteca cubre el 100% del precio de la vivienda.")
        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    # 4 Casos de Prueba con Errores
    def test_calcular_hipoteca_inversa_con_porcentajes_negativos(self):
        edad = 74
        expectativa_de_vida = 88
        años_de_renta = 14
        total_cuotas = 168
        precio_de_la_vivienda = 1_032_374_862
        porcentaje_precio_real = -5.0
        valor_de_la_hipoteca = 516_187_431
        tasa_de_interes_mensual = -2.8

        with self.assertRaises(hipoteca_inversa.ErrorValoresIngresadosPorcentajes) as comentario:
            hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)
        print("\nCaso de Error 1")
        print(f"Mensaje de error: El valor de los porcentajes de la vivienda y la tasa de interes son invalidos. Los Valores del porcentaje de la vivienda ({porcentaje_precio_real}) y/o ({tasa_de_interes_mensual}) no pueden ser negativos. Vuelvalo a intentar con valores positivos")

    def test_calcular_hipoteca_inversa_con_edad_invalida(self):
        edad = 50
        expectativa_de_vida = 90
        años_de_renta = 30
        total_cuotas = 360
        precio_de_la_vivienda = 825_899_890
        porcentaje_precio_real = 45
        valor_de_la_hipoteca = 371_654_951
        tasa_de_interes_mensual = 6

        with self.assertRaises(hipoteca_inversa.ErrorEdadIncorrecta) as comentario:
            hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)
        print("\nCaso de Error 2")
        print(f"Mensaje de error: El valor de la edad del cliente no es válida. La edad ingresada ({edad}) es incorrecta. Vuelvalo a intentar teniendo en cuenta que la edad minima para la hipoteca inversa es 65")

    def test_calcular_hipoteca_inversa_con_cuotas_invalida(self):
        edad = 80
        expectativa_de_vida = 92
        años_de_renta = 12
        total_cuotas = 0
        precio_de_la_vivienda = 1_238_849_835
        porcentaje_precio_real = 50
        valor_de_la_hipoteca = 619_424_918
        tasa_de_interes_mensual = 5

        with self.assertRaises(hipoteca_inversa.ErrorCuotas) as comentario:
            hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)
        print("\nCaso de Error 3")
        print(f"Mensaje de error: El valor de las cuotas no es válido. El numero de cuotas ({total_cuotas}) es incorrecta. Vuelvalo a intentar sabiendo que el numero de cuotas no puede ser negativo o igual que 0, sepa que el valor debe ser mayor que 0")

    def test_calcular_hipoteca_inversa_con_edad_negativa(self):
        edad = -65
        expectativa_de_vida = 79
        años_de_renta = 14
        total_cuotas = 168
        precio_de_la_vivienda = 619_424_917
        porcentaje_precio_real = 40
        valor_de_la_hipoteca = 247_769_967
        tasa_de_interes_mensual = 2.3

        with self.assertRaises(hipoteca_inversa.ErrorEdadnegativa) as comentario:
            hipoteca_inversa.Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)
        print("\nCaso de Error 4")
        print(f"Mensaje de error: La edad ingresada no puede ser negativa. La edad ingresada ({edad}) es incorrecta. Vuelvalo a intentar teniendo en cuenta que la edad no debe ser negativa")

if __name__ == '__main__':
    unittest.main()