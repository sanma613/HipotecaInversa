import unittest
import hipoteca_inversa

class PruebasHipotecaInversa(unittest.TestCase):
    
    def test_calculos_hipoteca_inversa_1(self):
        edad = 70
        expectativa_de_vida = 75
        años_de_renta = 5
        total_cuotas = 60
        precio_de_la_vivienda = 200000000
        porcentaje_precio_real = 30
        valor_de_la_hipoteca = 60000000
        tasa_de_interes_mensual = 10

        resultado_ingreso_mensual_esperado = 1000000
        resultado_deuda_total_esperada = 3338298035

        ingreso_mensual = hipoteca_inversa.calcular_ingreso_mensual(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas)
        deuda_total = hipoteca_inversa.calcular_deuda_total(ingreso_mensual, tasa_de_interes_mensual, total_cuotas)

        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    def test_calculos_hipoteca_inversa_2(self):
        edad = 75
        expectativa_de_vida = 88
        años_de_renta = 17
        total_cuotas = 156
        precio_de_la_vivienda = 412949945
        porcentaje_precio_real = 50
        valor_de_la_hipoteca = 206474973
        tasa_de_interes_mensual = 5.50

        resultado_ingreso_mensual_esperado = 1323558
        resultado_deuda_total_esperada = 107625171318

        ingreso_mensual = hipoteca_inversa.calcular_ingreso_mensual(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas)
        deuda_total = hipoteca_inversa.calcular_deuda_total(ingreso_mensual, tasa_de_interes_mensual, total_cuotas)

        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    def test_calculos_hipoteca_inversa_3(self):
        edad = 85
        expectativa_de_vida = 89
        años_de_renta = 4
        total_cuotas = 48
        precio_de_la_vivienda = 619424917
        porcentaje_precio_real = 40
        valor_de_la_hipoteca = 247769967
        tasa_de_interes_mensual = 4.80

        resultado_ingreso_mensual_esperado = 5161874
        resultado_deuda_total_esperada = 957016422

        ingreso_mensual = hipoteca_inversa.calcular_ingreso_mensual(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas)
        deuda_total = hipoteca_inversa.calcular_deuda_total(ingreso_mensual, tasa_de_interes_mensual, total_cuotas)

        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    def test_calculos_hipoteca_inversa_total_cuotas_1(self):
        edad = 70
        expectativa_de_vida = 85
        años_de_renta = 20                                       
        total_cuotas = 1
        precio_de_la_vivienda = 908489879
        porcentaje_precio_real = 55
        valor_de_la_hipoteca = 499699433
        tasa_de_interes_mensual = 1.20

        resultado_ingreso_mensual_esperado = 499669433
        resultado_deuda_total_esperada = 505665467

        ingreso_mensual = hipoteca_inversa.calcular_ingreso_mensual(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas)
        deuda_total = hipoteca_inversa.calcular_deuda_total(ingreso_mensual, tasa_de_interes_mensual, total_cuotas)

        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    def test_calculos_hipoteca_inversa_tasa_de_interes_0(self):
        edad = 78
        expectativa_de_vida = 90
        años_de_renta = 12
        total_cuotas = 144
        precio_de_la_vivienda = 1238849835
        porcentaje_precio_real = 50
        valor_de_la_hipoteca = 619424918
        tasa_de_interes_mensual = 0

        resultado_ingreso_mensual_esperado = 4301562
        resultado_deuda_total_esperada = 619424918

        ingreso_mensual = hipoteca_inversa.calcular_ingreso_mensual(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas)
        deuda_total = hipoteca_inversa.calcular_deuda_total(ingreso_mensual, tasa_de_interes_mensual, total_cuotas)

        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    def test_calculos_hipoteca_inversa_hipoteca_100(self):
        edad = 76
        expectativa_de_vida = 88
        años_de_renta = 12
        total_cuotas = 144
        precio_de_la_vivienda = 743309901
        porcentaje_precio_real = 100
        valor_de_la_hipoteca = 743309901
        tasa_de_interes_mensual = 1.1

        resultado_ingreso_mensual_esperado = 5161874
        resultado_deuda_total_esperada = 1818198009

        ingreso_mensual = hipoteca_inversa.calcular_ingreso_mensual(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas)
        deuda_total = hipoteca_inversa.calcular_deuda_total(ingreso_mensual, tasa_de_interes_mensual, total_cuotas)

        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places=2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places=2)

    def test_porcentajes_negativos(self):
        edad = 74
        expectativa_de_vida = 88
        años_de_renta = 14
        total_cuotas = 168
        precio_de_la_vivienda = 1032374862
        porcentaje_precio_real = -50
        valor_de_la_hipoteca = 516187431
        tasa_de_interes_mensual = -2.8

        with self.assertRaises(hipoteca_inversa.ErrorValoresIngresadosPorcentajes) as cm:
            ingreso_mensual = hipoteca_inversa.calcular_ingreso_mensual(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas)
            deuda_total = hipoteca_inversa.calcular_deuda_total(ingreso_mensual, tasa_de_interes_mensual, total_cuotas)
        print(f"Mensaje de error: {cm.exception}")

    def test_edad_invalida(self):
        edad = 50
        expectativa_de_vida = 90
        años_de_renta = 30
        total_cuotas = 360
        precio_de_la_vivienda = 825899890
        porcentaje_precio_real = 45
        valor_de_la_hipoteca = 371654951
        tasa_de_interes_mensual = 6

        with self.assertRaises(hipoteca_inversa.ErrorEdadIncorrecta) as cm:
            ingreso_mensual = hipoteca_inversa.calcular_ingreso_mensual(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas)
            deuda_total = hipoteca_inversa.calcular_deuda_total(ingreso_mensual, tasa_de_interes_mensual, total_cuotas)
        print(f"Mensaje de error: {cm.exception}")

    def test_cuotas_invalida(self):
        edad = 80
        expectativa_de_vida = 92
        años_de_renta = 12
        total_cuotas = 0
        precio_de_la_vivienda = 1238849835
        porcentaje_precio_real = 50
        valor_de_la_hipoteca = 619424918
        tasa_de_interes_mensual = 5

        with self.assertRaises(hipoteca_inversa.ErrorCuotas) as cm:
            ingreso_mensual = hipoteca_inversa.calcular_ingreso_mensual(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas)
            deuda_total = hipoteca_inversa.calcular_deuda_total(ingreso_mensual, tasa_de_interes_mensual, total_cuotas)
        print(f"Mensaje de error: {cm.exception}")

    def test_edad_negativa(self):
        edad = -65
        expectativa_de_vida = 79
        años_de_renta = 14
        total_cuotas = 168
        precio_de_la_vivienda = 619424917
        porcentaje_precio_real = 40
        valor_de_la_hipoteca = 247769967
        tasa_de_interes_mensual = 2.3

        with self.assertRaises(hipoteca_inversa.ErrorEdadnegativa) as cm:
            ingreso_mensual = hipoteca_inversa.calcular_ingreso_mensual(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas)
            deuda_total = hipoteca_inversa.calcular_deuda_total(ingreso_mensual, tasa_de_interes_mensual, total_cuotas)
        print(f"Mensaje de error: {cm.exception}")

if __name__ == '__main__':
    unittest.main()