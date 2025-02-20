import unittest
import hipoteca_inversa

class PruebasHipotecaInversa(unittest.TestCase):

#3 Casos de prueba normales

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

        ingreso_mensual = hipoteca_inversa.calcular_ingreso_mensual(precio_de_la_vivienda, porcentaje_precio_real, total_cuotas)
        deuda_total = hipoteca_inversa.calcular_deuda_total(ingreso_mensual, tasa_de_interes_mensual, total_cuotas)

        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places = 2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places = 2)


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

        ingreso_mensual = hipoteca_inversa.calcular_ingreso_mensual(precio_de_la_vivienda, porcentaje_precio_real, total_cuotas)
        deuda_total = hipoteca_inversa.calcular_deuda_total(ingreso_mensual, tasa_de_interes_mensual, total_cuotas)

        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places = 2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places = 2)


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

        ingreso_mensual = hipoteca_inversa.calcular_ingreso_mensual(precio_de_la_vivienda, porcentaje_precio_real, total_cuotas)
        deuda_total = hipoteca_inversa.calcular_deuda_total(ingreso_mensual, tasa_de_interes_mensual, total_cuotas)

        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places = 2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places = 2)


#3 casos de pruebas extraordinarles

#1) Persona que vive mas de lo esperado (Tiene que pagar mas de lo normal)

    def test_persona_años_de_vida_extra (self):
        edad = 70
        expectativa_de_vida = 85
        años_de_renta = 20
        total_cuotas = 180
        precio_de_la_vivienda = 908489879
        porcentaje_precio_real = 55
        valor_de_la_hipoteca = 499699433
        tasa_de_interes_mensual = 1.20

        resultado_ingreso_mensual_esperado = 2775941
        resultado_deuda_total_esperada = 1769914434
        
        ingreso_mensual = hipoteca_inversa.calcular_ingreso_mensual(precio_de_la_vivienda, porcentaje_precio_real, total_cuotas)
        deuda_total = hipoteca_inversa.calcular_deuda_total(ingreso_mensual, tasa_de_interes_mensual, total_cuotas)

        
        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places = 2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places = 2)

#2) Caida extrema del valor de la vivienda (banco asume perdida completa)

    def test_caida_extrema (self):
        edad = 78
        expectativa_de_vida = 90
        años_de_renta = 12
        total_cuotas = 144
        precio_de_la_vivienda = 1238849835
        porcentaje_precio_real = 50
        valor_de_la_hipoteca = 619424918
        tasa_de_interes_mensual = 2.1

        resultado_ingreso_mensual_esperado = 4301562
        resultado_deuda_total_esperada = 3960895114
        
        ingreso_mensual = hipoteca_inversa.calcular_ingreso_mensual(precio_de_la_vivienda, porcentaje_precio_real, total_cuotas)
        deuda_total = hipoteca_inversa.calcular_deuda_total(ingreso_mensual, tasa_de_interes_mensual, total_cuotas)

        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places = 2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places = 2)


#3) Usuario ingresa a una residencia y pierde la casa (deuda sin posibilidad economica de pagar)

    def test_residencia (self):
        edad = 76
        expectativa_de_vida = 88
        años_de_renta = 12
        total_cuotas = 144
        precio_de_la_vivienda = 743309901
        porcentaje_precio_real = 50
        valor_de_la_hipoteca = 371654951
        tasa_de_interes_mensual = 1.1

        resultado_ingreso_mensual_esperado = 2580937
        resultado_deuda_total_esperada = 909099005
        
        ingreso_mensual = hipoteca_inversa.calcular_ingreso_mensual(precio_de_la_vivienda, porcentaje_precio_real, total_cuotas)
        deuda_total = hipoteca_inversa.calcular_deuda_total(ingreso_mensual, tasa_de_interes_mensual, total_cuotas)

        print(f"Ingreso mensual calculado: {ingreso_mensual}")
        print(f"Deuda total calculada: {deuda_total}")

        self.assertAlmostEqual(round(ingreso_mensual), resultado_ingreso_mensual_esperado, places = 2)
        self.assertAlmostEqual(round(deuda_total), resultado_deuda_total_esperada, places = 2)


if __name__ == '__main__':
    unittest.main()