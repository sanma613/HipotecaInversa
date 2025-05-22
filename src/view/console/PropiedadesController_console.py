import sys
sys.path.append("src")
from controller.PropiedadesController import PropiedadesController
from model.propiedades import Propiedad
from datetime import datetime

def mostrar_menu():
    print("\n¿Qué deseas hacer? Selecciona el número correspondiente:")
    print("1. Insertar propiedad")
    print("2. Buscar propiedad por ID")
    print("3. Modificar propiedad")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Opción: ")

    if opcion == "1":
        try:
            direccion = input("Ingrese la dirección: ")
            valor = float(input("Ingrese el valor estimado: "))
            tipo = input("Ingrese el tipo de propiedad: ")
            propietario_id = int(input("Ingrese el ID del propietario (cliente): "))
            fecha_registro = input("Ingrese la fecha de registro (YYYY-MM-DD HH:MM:SS): ")
            propiedad = Propiedad(
                None, direccion, valor, tipo, propietario_id, fecha_registro
            )
            PropiedadesController.insertar(propiedad)
            print("¡Propiedad insertada exitosamente!")
        except Exception as e:
            print(f"Error al insertar propiedad: {e}")

    elif opcion == "2":
        try:
            id_propiedad = int(input("Ingrese el ID de la propiedad para buscar: "))
            resultado = PropiedadesController.buscar_propiedad(id_propiedad)
            if resultado:
                print("Propiedad encontrada:", resultado)
            else:
                print("Propiedad no encontrada.")
        except Exception as e:
            print(f"Error al buscar propiedad: {e}")

    elif opcion == "3":
        try:
            id_propiedad = int(input("ID de la propiedad a modificar: "))
            propiedad = PropiedadesController.buscar_propiedad(id_propiedad)
            if not propiedad:
                print("Propiedad no encontrada.")
                continue

            print("\n¿Qué dato desea modificar?")
            print("1. Dirección")
            print("2. Valor estimado")
            print("3. Tipo")
            print("4. Propietario (cliente)")
            print("5. Fecha de registro")
            campo = input("Opción (1-5): ")
            nuevo_valor = input("Nuevo valor: ")

            if campo == "1":
                propiedad.direccion = nuevo_valor
            elif campo == "2":
                propiedad.valor = float(nuevo_valor)
            elif campo == "3":
                propiedad.tipo = nuevo_valor
            elif campo == "4":
                propiedad.propietario_id = int(nuevo_valor)
            elif campo == "5":
                propiedad.fecha_registro = nuevo_valor
            else:
                print("Opción no válida")
                continue

            PropiedadesController.eliminar_tabla()
            PropiedadesController.crear_tabla()
            PropiedadesController.insertar(propiedad)
            print("¡Dato actualizado!")
        except ValueError:
            print("Error: Ingrese valores válidos")
        except Exception as e:
            print(f"Error al modificar propiedad: {e}")

    elif opcion == "4":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Intente de nuevo.")