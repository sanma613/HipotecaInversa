import sys
sys.path.append("src")
from model.hipoteca_inversa import Hipoteca

#Se añade la consola, la cual pide los datos y calcula la deuda esperada y el ingreso mensual esperado

try:
    edad = int(input("Ingrese la edad del cliente: "))
    total_cuotas = int(input("Ingrese el total de cuotas: "))
    precio_de_la_vivienda = float(input("Ingrese el precio de la vivienda: "))
    porcentaje_precio_real = float(input("Ingrese el porcentaje del precio real a pagar de la vivienda: ")) 
    tasa_de_interes_mensual = float(input("Ingrese la tasa de interés mensual: ")) 

    hipoteca = Hipoteca(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual)

    resultado_ingreso_mensual_esperado = hipoteca.calcular_ingreso_mensual()
    resultado_deuda_total_esperada = hipoteca.calcular_deuda_total(resultado_ingreso_mensual_esperado)

    print(f"Ingreso mensual esperado: {resultado_ingreso_mensual_esperado}")
    print(f"Deuda total esperada: {resultado_deuda_total_esperada}")

except Exception as excepcion_de_error:
    print("Hubo un error en los datos ingresados:")
    print(str(excepcion_de_error))