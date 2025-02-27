def hipoteca_inversa_caso_1():
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

    ingreso_mensual = calcular_ingreso_mensual(precio_de_la_vivienda, porcentaje_precio_real, total_cuotas)
    deuda_total = calcular_deuda_total(ingreso_mensual, tasa_de_interes_mensual, total_cuotas)

    print(f"Ingreso mensual calculado: {ingreso_mensual}")
    print(f"Deuda total calculada: {deuda_total}")

    if round(ingreso_mensual) == resultado_ingreso_mensual_esperado:
        print("Está correcto el ingreso mensual")
    else:
        print("Está incorrecto el ingreso mensual")
        print(f"Se obtuvo: {round(ingreso_mensual)} y se esperaba {resultado_ingreso_mensual_esperado}")

    if round(deuda_total) == resultado_deuda_total_esperada:
        print("Está correcta la deuda total")
    else:
        print("Está incorrecta la deuda total")
        print(f"Se obtuvo: {round(deuda_total)} y se esperaba {resultado_deuda_total_esperada}")

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

hipoteca_inversa_caso_1()


def hipoteca_inversa_caso_2():
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

    ingreso_mensual = calcular_ingreso_mensual(precio_de_la_vivienda, porcentaje_precio_real, total_cuotas)
    deuda_total = calcular_deuda_total(ingreso_mensual, tasa_de_interes_mensual, total_cuotas)

    print(f"Ingreso mensual calculado: {ingreso_mensual}")
    print(f"Deuda total calculada: {deuda_total}")

    if round(ingreso_mensual) == resultado_ingreso_mensual_esperado:
        print("Está correcto el ingreso mensual")
    else:
        print("Está incorrecto el ingreso mensual")
        print(f"Se obtuvo: {round(ingreso_mensual)} y se esperaba {resultado_ingreso_mensual_esperado}")

    if round(deuda_total) == resultado_deuda_total_esperada:
        print("Está correcta la deuda total")
    else:
        print("Está incorrecta la deuda total")
        print(f"Se obtuvo: {round(deuda_total)} y se esperaba {resultado_deuda_total_esperada}")

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

hipoteca_inversa_caso_2()


def hipoteca_inversa_caso_3():
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

    ingreso_mensual = calcular_ingreso_mensual(precio_de_la_vivienda, porcentaje_precio_real, total_cuotas)
    deuda_total = calcular_deuda_total(ingreso_mensual, tasa_de_interes_mensual, total_cuotas)

    print(f"Ingreso mensual calculado: {ingreso_mensual}")
    print(f"Deuda total calculada: {deuda_total}")

    if round(ingreso_mensual) == resultado_ingreso_mensual_esperado:
        print("Está correcto el ingreso mensual")
    else:
        print("Está incorrecto el ingreso mensual")
        print(f"Se obtuvo: {round(ingreso_mensual)} y se esperaba {resultado_ingreso_mensual_esperado}")

    if round(deuda_total) == resultado_deuda_total_esperada:
        print("Está correcta la deuda total")
    else:
        print("Está incorrecta la deuda total")
        print(f"Se obtuvo: {round(deuda_total)} y se esperaba {resultado_deuda_total_esperada}")

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

hipoteca_inversa_caso_3()