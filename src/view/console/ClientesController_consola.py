import sys
sys.path.append("src")
from controller.ClientesController import ClientesController
from model.Clientes import Cliente
from datetime import datetime



def mostrar_menu():
    print("\n¿Qué deseas hacer? Selecciona el número correspondiente:")
    print("1. Insertar cliente")
    print("2. Buscar cliente por ID")
    print("3. Modificar cliente")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Opción: ")

    if opcion == "1":
        try:
            id_cliente = int(input("Ingrese el ID del cliente: "))
            nombre = input("Ingrese el nombre: ")
            edad = int(input("Ingrese la edad: "))
            direccion = input("Ingrese la dirección: ")
            telefono = input("Ingrese el teléfono: ")
            email = input("Ingrese el email: ")
            fecha_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cliente = Cliente(id_cliente, nombre, edad, direccion, telefono, email, fecha_registro)
            ClientesController.insertar(cliente)
            print("¡Cliente insertado exitosamente!")
        except Exception as e:
            print(f"Error al insertar cliente: {e}")

    elif opcion == "2":
        try:
            id_cliente = int(input("Ingrese el ID del cliente para buscar: "))
            resultado = ClientesController.buscar_cliente(id_cliente)
            if resultado:
                print("Cliente encontrado:", resultado)
            else:
                print("Cliente no encontrado.")
        except Exception as e:
            print(f"Error al buscar cliente: {e}")

    elif opcion == "3":
        try:
            id_cliente = int(input("ID del cliente a modificar: "))
            cliente = ClientesController.buscar_cliente(id_cliente)
            if not cliente:
                print("Cliente no encontrado.")
                continue

            print("\n¿Qué dato desea modificar?")
            print("1. Nombre")
            print("2. Edad")
            print("3. Dirección")
            print("4. Teléfono")
            print("5. Email")
            campo = input("Opción (1-5): ")
            nuevo_valor = input("Nuevo valor: ")

            if campo == "1":
                cliente.nombre = nuevo_valor
            elif campo == "2":
                cliente.edad = int(nuevo_valor)
            elif campo == "3":
                cliente.direccion = nuevo_valor
            elif campo == "4":
                cliente.telefono = nuevo_valor
            elif campo == "5":
                cliente.email = nuevo_valor
            else:
                print("Opción no válida")
                continue

            ClientesController.eliminar_tabla()
            ClientesController.crear_tabla()
            ClientesController.insertar(cliente)
            print("¡Dato actualizado!")
        except ValueError:
            print("Error: Ingrese valores válidos")
        except Exception as e:
            print(f"Error al modificar cliente: {e}")

    elif opcion == "4":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Intente de nuevo.")