def calcular_ingreso_mensual(precio_de_la_vivienda, porcentaje_precio_real, total_cuotas):
    porcentaje_precio_real_porcentual = porcentaje_precio_real / 100
    valor_de_la_hipoteca = precio_de_la_vivienda * porcentaje_precio_real_porcentual
    ingreso_mensual = valor_de_la_hipoteca / total_cuotas
    return ingreso_mensual

def calcular_deuda_total(ingreso_mensual, tasa_de_interes_mensual, total_cuotas):
    tasa_de_interes_mensual_decimal = tasa_de_interes_mensual / 100
    saldo = 0

    for i in range(total_cuotas):
        saldo += ingreso_mensual
        interes = saldo * tasa_de_interes_mensual_decimal
        saldo += interes
    
    return round(saldo)  