class ErrorValoresIngresadosPorcentajes (Exception):
    def __init__(self, porcentaje_precio_real, tasa_de_interes_mensual):
        super().__init__(f"El valor de los porcentajes de la vivienda y la tasa de interes son invalidos. Los Valores del porcentaje de la vivienda ({tasa_de_interes_mensual}) y/o ({porcentaje_precio_real}) no pueden ser negativos. Vuelvalo a intentar con valores positivos")

class ErrorEdadIncorrecta (Exception):
    def __init__(self, edad):
        super().__init__(f"El valor de la edad del cliente no es válida. La edad ingresada ({edad}) es incorrecta. Vuelvalo a intentar teniendo en cuenta que la edad minima para la hipoteca inversa es 65")

class ErrorCuotas (Exception):
    def __init__(self, total_cuotas):
        super().__init__(f"El valor de las cuotas no es válido. El numero de cuotas ({total_cuotas}) es incorrecta. Vuelvalo a intentar sabiendo que el numero de cuotas no puede ser negativo o igual que 0, sepa que el valor debe ser mayor que 0")

class ErrorEdadnegativa (Exception):
    def __init__(self, edad):
        super().__init__(f"La edad ingresada no puede ser negativa. La edad ingresada ({edad}) es incorrecta. Vuelvalo a intentar teniendo en cuenta que la edad no debe ser negativa")


def calcular_ingreso_mensual(edad, precio_de_la_vivienda, porcentaje_precio_real, total_cuotas, tasa_de_interes_mensual):
    if edad < 0:
        raise ErrorEdadnegativa(edad)
    
    if edad < 65:
        raise ErrorEdadIncorrecta (edad)
    
    
    if total_cuotas <= 0:
        raise ErrorCuotas(total_cuotas)
    
    if porcentaje_precio_real < 0:
        raise ErrorValoresIngresadosPorcentajes(porcentaje_precio_real, tasa_de_interes_mensual)
    
    
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


def calcular_deuda_total(ingreso_mensual, tasa_de_interes_mensual, total_cuotas, porcentaje_precio_real):

    if total_cuotas <= 0:
        raise ErrorCuotas(total_cuotas)
    
    if tasa_de_interes_mensual < 0:
        raise ErrorValoresIngresadosPorcentajes(porcentaje_precio_real, tasa_de_interes_mensual)

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