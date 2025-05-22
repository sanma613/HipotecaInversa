import sys
sys.path.append("src")
from controller.PagosController import PagosController
from model.Pagos import Pago
from datetime import datetime

def mostrar_menu():
    print("\n¿Qué deseas hacer? Selecciona el número correspondiente:")
    print("1. Insertar pago")
    print("2. Buscar pago por ID")
    print("3. Modificar pago")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Opción: ")

    if opcion == "1":
        try:
            hipoteca_id = int(input("Ingrese el ID de la hipoteca: "))
            monto = float(input("Ingrese el monto del pago: "))
            fecha_pago = input("Ingrese la fecha de pago (YYYY-MM-DD HH:MM:SS): ")
            pago = Pago(None, hipoteca_id, monto, fecha_pago)
            PagosController.insertar(pago)
            print("¡Pago insertado exitosamente!")
        except Exception as e:
            print(f"Error al insertar pago: {e}")

    elif opcion == "2":
        try:
            id_pago = int(input("Ingrese el ID del pago para buscar: "))
            resultado = PagosController.buscar_pago(id_pago)
            if resultado:
                print("Pago encontrado:", resultado)
            else:
                print("Pago no encontrado.")
        except Exception as e:
            print(f"Error al buscar pago: {e}")

    elif opcion == "3":
        try:
            id_pago = int(input("ID del pago a modificar: "))
            pago = PagosController.buscar_pago(id_pago)
            if not pago:
                print("Pago no encontrado.")
                continue

            print("\n¿Qué dato desea modificar?")
            print("1. Monto")
            print("2. Fecha de pago")
            campo = input("Opción (1-2): ")
            nuevo_valor = input("Nuevo valor: ")

            if campo == "1":
                pago.monto = float(nuevo_valor)
            elif campo == "2":
                pago.fecha_pago = nuevo_valor
            else:
                print("Opción no válida")
                continue

            PagosController.eliminar_tabla()
            PagosController.crear_tabla()
            PagosController.insertar(pago)
            print("¡Dato actualizado!")
        except ValueError:
            print("Error: Ingrese valores válidos")
        except Exception as e:
            print(f"Error al modificar pago: {e}")

    elif opcion == "4":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Intente de nuevo.")