import hipoteca_inversa

try:
    edad = int(input("Ingrese la edad del cliente: "))
    expectativa_de_vida = int(input("Ingrese la expectativa de vida del cliente: "))
    años_de_renta = int(input("Ingrese los años de renta del cliente: "))
    total_cuotas = int(input("Ingrese el total de cuotas: "))
    precio_de_la_vivienda = float(input("Ingrese el precio de la vivienda: "))
    porcentaje_precio_real = float(input("Ingrese el porcentaje del precio real: ")) 
    valor_de_la_hipoteca = float(input("Ingrese el valor de la hipoteca: "))
    tasa_de_interes_mensual = float(input("Ingrese la tasa de interés mensual: ")) 


    resultado_ingreso_mensual_esperado = hipoteca_inversa.calcular_ingreso_mensual(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas)
    resultado_deuda_total_esperada = hipoteca_inversa.calcular_deuda_total(resultado_ingreso_mensual_esperado, tasa_de_interes_mensual, total_cuotas)

    print(f"Ingreso mensual esperado: {resultado_ingreso_mensual_esperado}")
    print(f"Deuda total esperada: {resultado_deuda_total_esperada}")

except Exception as e:
    print("Hubo un error en los datos ingresados:")
    print(str(e))