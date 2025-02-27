class ErrorValoresIngresadosPorcentajes (Exception):
    """El valor de los porcentajes de la vivienda y la tasa de interes no pueden ser negativos."""

class ErrorEdadIncorrecta (Exception):
    """El valor de la edad del cliente no es válida."""

class ErrorCuotas (Exception):
    """El valor de las cuotas no es válido."""

class ErrorEdadnegativa (Exception):
    """La edad no puede ser negativa."""

def calcular_ingreso_mensual(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas):
    if edad < 0:
        raise ErrorEdadnegativa("La edad no puede ser negativa.")
    
    if edad < 65:
        raise ErrorEdadIncorrecta("El valor de la edad del cliente no es válida.")
    
    
    if total_cuotas <= 0:
        raise ErrorCuotas("El valor de las cuotas no es válido.")
    
    if porcentaje_precio_real < 0:
        raise ErrorValoresIngresadosPorcentajes("El valor de los porcentajes de la vivienda y la tasa de interes no pueden ser negativos.")
    
    
    porcentaje_precio_real_porcentual = porcentaje_precio_real / 100
    valor_de_la_hipoteca = precio_de_la_vivienda * porcentaje_precio_real_porcentual
    ingreso_mensual = valor_de_la_hipoteca / total_cuotas

    if porcentaje_precio_real == 100:
        print("Advertencia: La hipoteca cubre el 100% del precio de la vivienda.")

    if total_cuotas == 1:
        ingreso_mensual = valor_de_la_hipoteca
    else:
        ingreso_mensual = valor_de_la_hipoteca / total_cuotas

    return ingreso_mensual


def calcular_deuda_total(ingreso_mensual, tasa_de_interes_mensual, total_cuotas):

    if total_cuotas <= 0:
        raise ErrorCuotas("El valor de las cuotas no es válido.")
    
    if tasa_de_interes_mensual < 0:
        raise ErrorValoresIngresadosPorcentajes("El valor de los porcentajes de la vivienda y la tasa de interes no pueden ser negativos.")

    tasa_de_interes_mensual_decimal = tasa_de_interes_mensual / 100
    
    if tasa_de_interes_mensual == 0:
        saldo = ingreso_mensual * total_cuotas
        return saldo

    if total_cuotas == 1:
        interes = ingreso_mensual * tasa_de_interes_mensual_decimal
        saldo = ingreso_mensual + interes
    else:
        saldo = 0
        for i in range(total_cuotas):
            saldo += ingreso_mensual
            interes = saldo * tasa_de_interes_mensual_decimal
            saldo += interes

    return saldo