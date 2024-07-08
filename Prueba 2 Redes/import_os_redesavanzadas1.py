import os
import ipaddress

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
            print(f"{i} - {dispositivo}")
        dispositivo_elegido = int(input("Elija un dispositivo para ver más detalles: "))
        if 1 <= dispositivo_elegido <= len(dispositivos):
            if sector == 1:  # Sucursal Principal
                if dispositivo_elegido == 1:  # Router seleccionado
                    leer_archivo_routersucursal()
                elif dispositivo_elegido == 2:  # Switch Multicapa seleccionado
                    leer_archivo_switchmulticapa()
                elif dispositivo_elegido == 3:  # Dispositivos Finales seleccionado
                    leer_archivo_dispositivofinal()
                else:
                    print(f"Detalles del dispositivo: {dispositivos[dispositivo_elegido - 1]}")
            elif sector == 2:  # Backbone
                if dispositivo_elegido == 1:  # Router seleccionado
                    leer_archivo_routerblackbone()
                else:
                    print(f"Detalles del dispositivo: {dispositivos[dispositivo_elegido - 1]}")
            elif sector == 3:  # BGP 2345
                if dispositivo_elegido == 1:  # Router BGP 2345 seleccionado
                    leer_archivo_routerbgp2345()
                else:
                    print(f"Detalles del dispositivo: {dispositivos[dispositivo_elegido - 1]}")
            elif sector == 4:  # Oficina Remota
                if dispositivo_elegido == 1:  # Oficina Remota 1 seleccionado
                    leer_archivo_oficinaremota1()
                elif dispositivo_elegido == 2:  # Oficina Remota 2 seleccionado
                    leer_archivo_oficinaremota2()
                else:
                    print(f"Detalles del dispositivo: {dispositivos[dispositivo_elegido - 1]}")
            elif sector == 5:  # OSPF Area 123
                if dispositivo_elegido == 1:  # OSPF Area 123 seleccionado
                    leer_archivo_ospfarea123()
                else:
                    print(f"Detalles del dispositivo: {dispositivos[dispositivo_elegido - 1]}")
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

# Función para validar una máscara de Subred
def validar_subred(subred):
    try:
        ipaddress.ip_network(f'0.0.0.0/{subred}')
        return True
    except ValueError:
        return False

# Función para leer el archivo Routersucursal.txt
def leer_archivo_routersucursal():
    try:
        with open("Routersucursal.txt", "r") as file:
            contenido = file.read()
            print("Contenido de Routersucursal.txt:")
            print(contenido)
    except FileNotFoundError:
        print("El archivo Routersucursal.txt no se encuentra.")

# Función para leer el archivo Routerblackbone.txt
def leer_archivo_routerblackbone():
    try:
        with open("Routerblackbone.txt", "r") as file:
            contenido = file.read()
            print("Contenido de Routerblackbone.txt:")
            print(contenido)
    except FileNotFoundError:
        print("El archivo Routerblackbone.txt no se encuentra.")

# Función para leer el archivo RouterBGP2345.txt
def leer_archivo_routerbgp2345():
    try:
        with open("RouterBGP2345.txt", "r") as file:
            contenido = file.read()
            print("Contenido de RouterBGP2345.txt:")
            print(contenido)
    except FileNotFoundError:
        print("El archivo RouterBGP2345.txt no se encuentra.")

# Función para leer el archivo oficina remota 1.txt
def leer_archivo_oficinaremota1():
    try:
        with open("oficina remota 1.txt", "r") as file:
            contenido = file.read()
            print("Contenido de oficina remota 1.txt:")
            print(contenido)
    except FileNotFoundError:
        print("El archivo oficina remota 1.txt no se encuentra.")

# Función para leer el archivo oficina remota 2.txt
def leer_archivo_oficinaremota2():
    try:
        with open("oficina remota 2.txt", "r") as file:
            contenido = file.read()
            print("Contenido de oficina remota 2.txt:")
            print(contenido)
    except FileNotFoundError:
        print("El archivo oficina remota 2.txt no se encuentra.")

# Función para leer el archivo switchmulticapa.txt
def leer_archivo_switchmulticapa():
    try:
        with open("switchmulticapa.txt", "r") as file:
            contenido = file.read()
            print("Contenido de switchmulticapa.txt:")
            print(contenido)
    except FileNotFoundError:
        print("El archivo switchmulticapa.txt no se encuentra.")

# Función para leer el archivo dispositivofinal.txt
def leer_archivo_dispositivofinal():
    try:
        with open("dispositivofinal.txt", "r") as file:
            contenido = file.read()
            print("Contenido de dispositivofinal.txt:")
            print(contenido)
    except FileNotFoundError:
        print("El archivo dispositivofinal.txt no se encuentra.")

# Función para leer el archivo OSPF Area 123.txt
def leer_archivo_ospfarea123():
    try:
        with open("OSPF Area 123.txt", "r") as file:
            contenido = file.read()
            print("Contenido de OSPF Area 123.txt:")
            print(contenido)
    except FileNotFoundError:
        print("El archivo OSPF Area 123.txt no se encuentra.")

# Función para generar los archivos solicitados
def generar_archivos_txt():
    archivos_contenidos = {
        "internet.txt": "Contenido del archivo internet.txt",
        "oficina remota 5-6.txt": "Contenido del archivo oficina remota 5-6.txt",
        "oficina remota 3-4.txt": "Contenido del archivo oficina remota 3-4.txt"
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
            print(f"{i} - {dispositivo}")
        dispositivo_elegido = int(input("Elija el número del dispositivo a borrar: "))
        if 1 <= dispositivo_elegido <= len(dispositivos):
            dispositivo_borrado = dispositivos.pop(dispositivo_elegido - 1)
            print(f"Dispositivo '{dispositivo_borrado}' borrado con éxito.")
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
        subred = input("Ingrese la máscara de subred del nuevo dispositivo : ")
        while not validar_subred(subred):
            print("Máscara de subred no válida. Intente de nuevo.")
            subred = input("Ingrese la máscara de subred del nuevo dispositivo : ")
        vlan = input("Ingrese la VLAN del nuevo dispositivo: ")
        modelo = input("Ingrese el modelo jerárquico del nuevo dispositivo: ")
        servicios = input("Ingrese los servicios del nuevo dispositivo: ")

        nuevo_dispositivo = {
            'nombre': nombre,
            'ip': ip,
            'subred': subred,
            'vlan': vlan,
            'modelo': modelo,
            'servicios': servicios
        }
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
    1: {'nombre': "Sucursal Principal", 'dispositivos': ["Router", "Switch Multicapa", "Dispositivos Finales"]},
    2: {'nombre': "Backbone", 'dispositivos': ["Router", "Switch Multicapa", "Dispositivos Finales"]},
    3: {'nombre': "BGP 2345", 'dispositivos': ["Router BGP 2345", "Switch Multicapa", "Dispositivos Finales"]},
    4: {'nombre': "Oficina Remota", 'dispositivos': ["Oficina Remota 1", "Oficina Remota 2", "Switch Multicapa", "Dispositivos Finales"]},
    5: {'nombre': "OSPF Area 123", 'dispositivos': ["OSPF Area 123"]}
}

# Generar los archivos solicitados al inicio del programa
generar_archivos_txt()

while True:
    clear_screen()
    print("Bienvenido, ¿qué desea hacer?")
    print("1-ver sectores\n2-ver dispositivos\n3-borrar dispositivos\n4-borrar sectores\n5-añadir sectores\n6-añadir dispositivos\n7-salir")
    opciones = int(input("Elija una opción: "))
    clear_screen()

    if opciones == 1:
        mostrar_sectores(dispositivos_por_sector)
    elif opciones == 2:
        mostrar_sectores(dispositivos_por_sector)
        sector = int(input("Elija un sector: "))
        clear_screen()
        mostrar_dispositivos(sector, dispositivos_por_sector)
    elif opciones == 3:
        mostrar_sectores(dispositivos_por_sector)
        sector = int(input("Elija un sector: "))
        clear_screen()
        borrar_dispositivo(sector, dispositivos_por_sector)
    elif opciones == 4:
        borrar_sector(dispositivos_por_sector)
    elif opciones == 5:
        añadir_sector(dispositivos_por_sector)
    elif opciones == 6:
        mostrar_sectores(dispositivos_por_sector)
        sector = int(input("Elija un sector: "))
        clear_screen()
        añadir_dispositivo(sector, dispositivos_por_sector)
    elif opciones == 7:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida.")

    input("\nPresione Enter para continuar...")