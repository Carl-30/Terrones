import os
import ipaddress
import json

# Función para limpiar la pantalla de manera compatible con diferentes sistemas operativos
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Función para mostrar dispositivos de un sector
def mostrar_dispositivos(sector, dispositivos_por_sector):
    if sector in dispositivos_por_sector:
        print("Dispositivos en el sector seleccionado:")
        dispositivos = dispositivos_por_sector[sector]['dispositivos']
        for i, dispositivo in enumerate(dispositivos, 1):
            print(f"{i} - {dispositivo['nombre']}")
        dispositivo_elegido = int(input("Elija un dispositivo para ver más detalles: "))
        if 1 <= dispositivo_elegido <= len(dispositivos):
            dispositivo = dispositivos[dispositivo_elegido - 1]
            print(f"Detalles del dispositivo: {json.dumps(dispositivo, indent=4)}")
            if 'archivo' in dispositivo:
                leer_archivo(dispositivo['archivo'])
        else:
            print("Dispositivo no válido.")
    else:
        print("Sector no válido.")

# Función para validar una dirección IP
def validar_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

# Función para validar una máscara de red
def validar_mascara(mascara):
    try:
        ipaddress.IPv4Network(f"0.0.0.0/{mascara}")
        return True
    except ValueError:
        return False

# Función para leer archivos específicos
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as file:
            contenido = file.read()
            print(f"Contenido de {nombre_archivo}:")
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encuentra.")

# Función para generar los archivos solicitados
def generar_archivos_txt():
    archivos_contenidos = {
        "Routerdistribucion.txt": "Contenido del archivo Routerdistribucion.txt",
        "switchmulticapa.txt": "Contenido del archivo switchmulticapa.txt",
        "dispositivofinal.txt": "Contenido del archivo dispositivofinal.txt"
    }
    
    for nombre_archivo, contenido in archivos_contenidos.items():
        with open(nombre_archivo, "w") as file:
            file.write(contenido)
        print(f"Archivo {nombre_archivo} generado con éxito.")

# Función para borrar dispositivos de un sector
def borrar_dispositivo(sector, dispositivos_por_sector):
    if sector in dispositivos_por_sector:
        print("Dispositivos en el sector seleccionado:")
        dispositivos = dispositivos_por_sector[sector]['dispositivos']
        for i, dispositivo in enumerate(dispositivos, 1):
            print(f"{i} - {dispositivo['nombre']}")
        dispositivo_elegido = int(input("Elija el número del dispositivo a borrar: "))
        if 1 <= dispositivo_elegido <= len(dispositivos):
            dispositivo_borrado = dispositivos.pop(dispositivo_elegido - 1)
            print(f"Dispositivo '{dispositivo_borrado['nombre']}' borrado con éxito.")
        else:
            print("Número de dispositivo no válido.")
    else:
        print("Sector no válido.")

# Función para añadir dispositivos a un sector
def añadir_dispositivo(sector, dispositivos_por_sector):
    if sector in dispositivos_por_sector:
        nombre = input("Ingrese el nombre del nuevo dispositivo: ")
        ip = input("Ingrese la IP del nuevo dispositivo: ")
        while not validar_ip(ip):
            print("IP no válida. Intente de nuevo.")
            ip = input("Ingrese la IP del nuevo dispositivo: ")
        vlan = input("Ingrese la VLAN del nuevo dispositivo: ")
        modelo = input("Ingrese el modelo jerárquico del nuevo dispositivo (Núcleo, Distribución, Acceso): ")
        while modelo not in ["Núcleo", "Distribución", "Acceso"]:
            print("Modelo jerárquico no válido. Intente de nuevo.")
            modelo = input("Ingrese el modelo jerárquico del nuevo dispositivo (Núcleo, Distribución, Acceso): ")
        servicios = input("Ingrese los servicios del nuevo dispositivo: ")
        archivo = input("Ingrese el nombre del archivo asociado (opcional): ")
        mascara = input("Ingrese la máscara de red del nuevo dispositivo (por ejemplo, 255.255.255.0): ")
        while not validar_mascara(mascara):
            print("Máscara de red no válida. Intente de nuevo.")
            mascara = input("Ingrese la máscara de red del nuevo dispositivo (por ejemplo, 255.255.255.0): ")

        nuevo_dispositivo = {
            'nombre': nombre,
            'ip': ip,
            'vlan': vlan,
            'modelo': modelo,
            'servicios': servicios,
            'mascara': mascara
        }
        if archivo:
            nuevo_dispositivo['archivo'] = archivo

        dispositivos_por_sector[sector]['dispositivos'].append(nuevo_dispositivo)
        print(f"Dispositivo '{nombre}' añadido con éxito al sector {sector}.")
    else:
        print("Sector no válido.")

# Función para borrar sectores
def borrar_sector(dispositivos_por_sector):
    print("Sectores disponibles:")
    for sector, detalles in dispositivos_por_sector.items():
        print(f"{sector} - {detalles['nombre']}")
    sector_elegido = int(input("Elija el número del sector a borrar: "))
    if sector_elegido in dispositivos_por_sector:
        del dispositivos_por_sector[sector_elegido]
        print(f"Sector {sector_elegido} borrado con éxito.")
    else:
        print("Número de sector no válido.")

# Función para añadir sectores
def añadir_sector(dispositivos_por_sector):
    nuevo_sector = int(input("Ingrese el número del nuevo sector: "))
    if nuevo_sector not in dispositivos_por_sector:
        nombre_sector = input("Ingrese el nombre del nuevo sector: ")
        dispositivos_por_sector[nuevo_sector] = {
            'nombre': nombre_sector,
            'dispositivos': []
        }
        print(f"Sector {nuevo_sector} ('{nombre_sector}') añadido con éxito.")
    else:
        print(f"El sector {nuevo_sector} ya existe.")

# Función para mostrar sectores
def mostrar_sectores(dispositivos_por_sector):
    print("Sectores disponibles:")
    for sector, detalles in dispositivos_por_sector.items():
        print(f"{sector} - {detalles['nombre']}")

# Diccionario para almacenar los dispositivos por sector
dispositivos_por_sector = {
    2: {
        'nombre': "Distribución",
        'dispositivos': [
            {'nombre': "Router Distribución", 'ip': "10.0.0.1", 'vlan': "40", 'modelo': "Distribución", 'servicios': "Enrutamiento", 'archivo': "Routerdistribucion.txt", 'mascara': "255.255.255.0"},
            {'nombre': "Switch Multicapa", 'ip': "10.0.0.2", 'vlan': "50", 'modelo': "Distribución", 'servicios': "Conmutación", 'archivo': "switchmulticapa.txt", 'mascara': "255.255.255.0"},
            {'nombre': "Dispositivos Finales", 'ip': "10.0.0.3", 'vlan': "60", 'modelo': "Acceso", 'servicios': "Acceso a red", 'archivo': "dispositivofinal.txt", 'mascara': "255.255.255.0"}
        ]
    }
}

# Menu principal
while True:
    clear_screen()
    print("1. Mostrar sectores")
    print("2. Añadir sector")
    print("3. Borrar sector")
    print("4. Mostrar dispositivos de un sector")
    print("5. Añadir dispositivo a un sector")
    print("6. Borrar dispositivo de un sector")
    print("7. Generar archivos solicitados")
    print("8. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        mostrar_sectores(dispositivos_por_sector)
    elif opcion == 2:
        añadir_sector(dispositivos_por_sector)
    elif opcion == 3:
        borrar_sector(dispositivos_por_sector)
    elif opcion == 4:
        sector = int(input("Ingrese el número del sector: "))
        mostrar_dispositivos(sector, dispositivos_por_sector)
    elif opcion == 5:
        sector = int(input("Ingrese el número del sector: "))
        añadir_dispositivo(sector, dispositivos_por_sector)
    elif opcion == 6:
        sector = int(input("Ingrese el número del sector: "))
        borrar_dispositivo(sector, dispositivos_por_sector)
    elif opcion == 7:
        generar_archivos_txt()
    elif opcion == 8:
        break
    else:
        print("Opción no válida.")
    
    input("Presione Enter para continuar...")
router 1