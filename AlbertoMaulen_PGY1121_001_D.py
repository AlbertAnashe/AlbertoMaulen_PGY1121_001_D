import datetime

# Variables globales
total_platinum = 0
total_gold = 0
total_silver = 0
asistentes = {}

# Funciones
def mostrar_menu():
    print("----- Menú -----")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
    print("-----------------")

def comprar_entradas():
    global total_platinum, total_gold, total_silver, asistentes
    cantidad = int(input("Ingrese la cantidad de entradas a comprar (1-3): "))
    if cantidad < 1 or cantidad > 3:
        print("Error: cantidad inválida")
        return

    print("Ubicaciones disponibles:")
    mostrar_ubicaciones_disponibles()

    for i in range(cantidad):
        ubicacion = int(input("Ingrese el número de ubicación deseada: "))
        if ubicacion < 1 or ubicacion > 100:
            print("Error: ubicación inválida")
            continue
        elif ubicacion in asistentes:
            print("Error: ubicación no disponible")
            continue

        run = input("Ingrese el RUN de la persona (sin guiones ni dígito verificador, 8 dígitos): ")
        if len(run) != 8:
            print("Error: el RUN debe tener 8 dígitos")
            continue

        asistentes[ubicacion] = run

        if ubicacion <= 20:
            total_platinum += 1
        elif ubicacion <= 50:
            total_gold += 1
        else:
            total_silver += 1

        print("Operación realizada correctamente")

def mostrar_ubicaciones_disponibles():
    print("----- Ubicaciones Disponibles -----")
    for i in range(1, 101):
        if i in asistentes:
            print("X", end=' ')
        else:
            print(i, end=' ')
        if i % 10 == 0:
            print()

def ver_listado_asistentes():
    print("----- Listado de Asistentes -----")
    asistentes_ordenados = sorted(asistentes.items(), key=lambda x: x[0])
    for ubicacion, run in asistentes_ordenados:
        print(f"Ubicación: {ubicacion} - RUN: {run}")

def mostrar_ganancias_totales():
    total = (total_platinum * 120000) + (total_gold * 80000) + (total_silver * 50000)
    print("----- Ganancias Totales -----")
    print("Entrada\t\tCantidad\tTotal")
    print("-----------------------------")
    print(f"Platinum (1-20)\t{total_platinum}\t${total_platinum * 120000}")
    print(f"Gold (21-50)\t{total_gold}\t${total_gold * 80000}")
    print(f"Silver (51-100)\t{total_silver}\t${total_silver * 50000}")
    print("-----------------------------")
    print(f"Total\t\t\t{total_platinum + total_gold + total_silver}\t${total}")

# Programa principal
print("¡Bienvenido a la venta de entradas para el concierto VIP de Michael Jam!")

while True:
    mostrar_menu()
    opcion = input("Ingrese una opción (1-5): ")

    if opcion == '1':
        comprar_entradas()
    elif opcion == '2':
        mostrar_ubicaciones_disponibles()
    elif opcion == '3':
        ver_listado_asistentes()
    elif opcion == '4':
        mostrar_ganancias_totales()
    elif opcion == '5':
        fecha_actual = datetime.date.today()
        print(f"¡Gracias por utilizar la aplicación! Fecha: {fecha_actual}")
        break
    else:
        print("Error: opción inválida")

#https://github.com/AlbertAnashe/AlbertoMaulen_PGY1121_001_D