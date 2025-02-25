def calcular_ingreso_mensual(precio_de_la_vivienda, porcentaje_precio_real, total_cuotas):
    porcentaje_precio_real_porcentual = porcentaje_precio_real / 100
    valor_de_la_hipoteca = precio_de_la_vivienda * porcentaje_precio_real_porcentual

    if porcentaje_precio_real == 100:
        print("Advertencia: La hipoteca cubre el 100% del precio de la vivienda.")

    if total_cuotas == 1:
        ingreso_mensual = valor_de_la_hipoteca
    else:
        ingreso_mensual = valor_de_la_hipoteca / total_cuotas

    return ingreso_mensual


def calcular_deuda_total(ingreso_mensual, tasa_de_interes_mensual, total_cuotas):
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