import sys
sys.path.append("src")
from controller.HipotecasController import HipotecasController
from model.Hipotecas import Hipoteca
from datetime import datetime

def mostrar_menu():
    print("\n¿Qué deseas hacer? Selecciona el número correspondiente:")
    print("1. Insertar hipoteca")
    print("2. Buscar hipoteca por ID")
    print("3. Modificar hipoteca")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Opción: ")

    if opcion == "1":
        try:
            id_hipoteca = int(input("Ingrese el ID de la hipoteca: "))
            cliente_id = int(input("Ingrese el ID del cliente: "))
            propiedad_id = int(input("Ingrese el ID de la propiedad: "))
            total_cuotas = int(input("Ingrese el total de cuotas: "))
            tasa_interes_mensual = float(input("Ingrese la tasa de interés mensual: "))
            ingreso_mensual = float(input("Ingrese el ingreso mensual: "))
            deuda_total = float(input("Ingrese la deuda total: "))
            fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD HH:MM:SS): ")
            estado = input("Ingrese el estado de la hipoteca: ")
            hipoteca = Hipoteca(
                id_hipoteca, cliente_id, propiedad_id, total_cuotas,
                tasa_interes_mensual, ingreso_mensual, deuda_total, fecha_inicio, estado
            )
            HipotecasController.insertar(hipoteca)
            print("¡Hipoteca insertada exitosamente!")
        except Exception as e:
            print(f"Error al insertar hipoteca: {e}")

    elif opcion == "2":
        try:
            id_hipoteca = int(input("Ingrese el ID de la hipoteca para buscar: "))
            resultado = HipotecasController.buscar_hipoteca(id_hipoteca)
            if resultado:
                print("Hipoteca encontrada:", resultado)
            else:
                print("Hipoteca no encontrada.")
        except Exception as e:
            print(f"Error al buscar hipoteca: {e}")

    elif opcion == "3":
        try:
            id_hipoteca = int(input("ID de la hipoteca a modificar: "))
            hipoteca = HipotecasController.buscar_hipoteca(id_hipoteca)
            if not hipoteca:
                print("Hipoteca no encontrada.")
                continue

            print("\n¿Qué dato desea modificar?")
            print("1. Total de cuotas")
            print("2. Tasa de interés mensual")
            print("3. Ingreso mensual")
            print("4. Deuda total")
            print("5. Fecha de inicio")
            print("6. Estado")
            campo = input("Opción (1-6): ")
            nuevo_valor = input("Nuevo valor: ")

            if campo == "1":
                hipoteca.total_cuotas = int(nuevo_valor)
            elif campo == "2":
                hipoteca.tasa_interes_mensual = float(nuevo_valor)
            elif campo == "3":
                hipoteca.ingreso_mensual = float(nuevo_valor)
            elif campo == "4":
                hipoteca.deuda_total = float(nuevo_valor)
            elif campo == "5":
                hipoteca.fecha_inicio = nuevo_valor
            elif campo == "6":
                hipoteca.estado = nuevo_valor
            else:
                print("Opción no válida")
                continue

            HipotecasController.eliminar_tabla()
            HipotecasController.crear_tabla()
            HipotecasController.insertar(hipoteca)
            print("¡Dato actualizado!")
        except ValueError:
            print("Error: Ingrese valores válidos")
        except Exception as e:
            print(f"Error al modificar hipoteca: {e}")

    elif opcion == "4":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Intente de nuevo.")